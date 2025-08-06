"""
Main Multi-Agent Software Development System
"""
import os
import json
from datetime import datetime
from typing import Dict, Any, List
from crewai import Crew, Process
from agents import AgentFactory
from tasks import TaskFactory
from config import Config

class MultiAgentSystem:
    """Main orchestrator for the multi-agent software development system"""
    
    def __init__(self):
        """Initialize the multi-agent system"""
        self.agent_factory = AgentFactory()
        self.task_factory = TaskFactory()
        self.workspace_dir = Config.WORKSPACE_DIR
        self.output_dir = Config.OUTPUT_DIR
        
        # Create necessary directories
        self._setup_directories()
        
        # Initialize agents
        self.software_developer = self.agent_factory.create_software_developer_agent()
        self.code_reviewer = self.agent_factory.create_code_reviewer_agent()
    
    def _setup_directories(self):
        """Create necessary directories"""
        os.makedirs(self.workspace_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_project(self, requirements: str, project_name: str = None) -> Dict[str, Any]:
        """Create a new project using the multi-agent system"""
        if not project_name:
            project_name = f"project_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        print(f"🚀 Starting project: {project_name}")
        print(f"📋 Requirements: {requirements[:100]}...")
        
        # Create project directory
        project_dir = os.path.join(self.output_dir, project_name)
        os.makedirs(project_dir, exist_ok=True)
        
        # Create tasks
        development_task = self.task_factory.create_development_task(
            self.software_developer, requirements, project_name
        )
        
        review_task = self.task_factory.create_review_task(
            self.code_reviewer, project_name
        )
        
        # Create crew
        crew = Crew(
            agents=[self.software_developer, self.code_reviewer],
            tasks=[development_task, review_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("🔄 Executing multi-agent workflow...")
        
        # Execute the crew
        result = crew.kickoff()
        
        # Save the complete result
        self._save_project_result(project_dir, requirements, str(result), project_name)
        
        print(f"✅ Project completed: {project_name}")
        print(f"📁 Project directory: {project_dir}")
        
        return {
            "project_name": project_name,
            "project_dir": project_dir,
            "requirements": requirements,
            "result": result
        }
    
    def _save_project_result(self, project_dir: str, requirements: str, result: str, project_name: str):
        """Save the complete project result with proper file structure"""
        
        # Save metadata
        metadata = {
            "project_name": project_name,
            "timestamp": datetime.now().isoformat(),
            "requirements": requirements,
            "model_used": self.agent_factory.llm.model,
            "agents": ["Software Developer", "Code Reviewer"],
            "project_dir": project_dir
        }
        
        with open(os.path.join(project_dir, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)
        
        # Save the complete result
        with open(os.path.join(project_dir, "result.txt"), "w") as f:
            f.write(result)
        
        # Extract and save code files from the result
        self._extract_code_files(project_dir, result)
        
        # Create a README for the project
        self._create_project_readme(project_dir, project_name, requirements)
    
    def _extract_code_files(self, project_dir: str, result: str):
        """Extract code files from the result and save them properly"""
        lines = result.split('\n')
        current_file = None
        current_content = []
        in_code_block = False
        
        for line in lines:
            # Look for code block markers
            if '```' in line:
                if in_code_block:
                    # End of code block
                    if current_file and current_content:
                        self._save_code_file(project_dir, current_file, current_content)
                    current_file = None
                    current_content = []
                    in_code_block = False
                else:
                    # Start of code block
                    in_code_block = True
                    # Try to extract filename from the line
                    if 'python' in line.lower() or '.py' in line:
                        current_file = 'main.py'
                    elif 'markdown' in line.lower() or 'md' in line:
                        current_file = 'README.md'
                    elif 'javascript' in line.lower() or '.js' in line:
                        current_file = 'app.js'
                    elif 'html' in line.lower() or '.html' in line:
                        current_file = 'index.html'
                    elif 'css' in line.lower() or '.css' in line:
                        current_file = 'style.css'
                    elif 'json' in line.lower() or '.json' in line:
                        current_file = 'config.json'
                    elif 'yaml' in line.lower() or '.yml' in line:
                        current_file = 'config.yml'
                    elif 'docker' in line.lower() or 'dockerfile' in line:
                        current_file = 'Dockerfile'
                    elif 'requirements' in line.lower() or 'dependencies' in line:
                        current_file = 'requirements.txt'
                    else:
                        current_file = 'code.txt'
            elif in_code_block and current_file:
                current_content.append(line)
        
        # Save any remaining code block
        if current_file and current_content:
            self._save_code_file(project_dir, current_file, current_content)
    
    def _save_code_file(self, project_dir: str, filename: str, content: List[str]):
        """Save a code file to the project directory"""
        filepath = os.path.join(project_dir, filename)
        with open(filepath, 'w') as f:
            f.write('\n'.join(content))
        print(f"📄 Saved: {filename}")
    
    def _create_project_readme(self, project_dir: str, project_name: str, requirements: str):
        """Create a README file for the project"""
        readme_content = f"""# {project_name}

## Project Overview
This project was generated by the Multi-Agent Software Development System using Gemma3:latest.

## Requirements
{requirements}

## Generated Files
- `result.txt` - Complete agent output and review
- `metadata.json` - Project metadata
- Various code files (see below)

## How to Use
1. Review the generated code files
2. Follow the instructions in the code comments
3. Install any required dependencies
4. Run the application according to the code instructions

## Generated by
- **Software Developer Agent**: Created the initial code and architecture
- **Code Reviewer Agent**: Provided quality assurance and improvement suggestions

## Model Used
- Gemma3:latest (via Ollama)

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        with open(os.path.join(project_dir, "PROJECT_README.md"), "w") as f:
            f.write(readme_content)
    
    def list_projects(self) -> List[Dict[str, Any]]:
        """List all completed projects"""
        projects = []
        
        if not os.path.exists(self.output_dir):
            return projects
        
        for project_dir in os.listdir(self.output_dir):
            project_path = os.path.join(self.output_dir, project_dir)
            if os.path.isdir(project_path):
                metadata_file = os.path.join(project_path, "metadata.json")
                if os.path.exists(metadata_file):
                    try:
                        with open(metadata_file, 'r') as f:
                            metadata = json.load(f)
                        projects.append(metadata)
                    except:
                        # If metadata is corrupted, create basic info
                        projects.append({
                            "project_name": project_dir,
                            "timestamp": "Unknown",
                            "requirements": "Unknown",
                            "model_used": "Unknown",
                            "agents": ["Unknown"],
                            "project_dir": project_path
                        })
        
        # Sort by timestamp (newest first)
        projects.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        return projects
    
    def get_project_details(self, project_name: str) -> Dict[str, Any]:
        """Get detailed information about a specific project"""
        project_dir = os.path.join(self.output_dir, project_name)
        
        if not os.path.exists(project_dir):
            raise FileNotFoundError(f"Project '{project_name}' not found")
        
        # Load metadata
        metadata_file = os.path.join(project_dir, "metadata.json")
        metadata = {}
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
        
        # Load result
        result_file = os.path.join(project_dir, "result.txt")
        result = ""
        if os.path.exists(result_file):
            with open(result_file, 'r') as f:
                result = f.read()
        
        # List all files in the project
        files = []
        for filename in os.listdir(project_dir):
            filepath = os.path.join(project_dir, filename)
            if os.path.isfile(filepath):
                files.append(filename)
        
        return {
            "metadata": metadata,
            "result": result,
            "files": files,
            "project_dir": project_dir
        } 