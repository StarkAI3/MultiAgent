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
        # First, try to extract Python code specifically
        python_code = self._extract_python_code(result)
        if python_code:
            with open(os.path.join(project_dir, 'main.py'), 'w') as f:
                f.write(python_code)
            print(f"📄 Saved: main.py")
        
        # Extract README content
        readme_content = self._extract_readme_content(result)
        if readme_content:
            with open(os.path.join(project_dir, 'README.md'), 'w') as f:
                f.write(readme_content)
            print(f"📄 Saved: README.md")
        
        # Extract requirements.txt if mentioned
        requirements_content = self._extract_requirements_content(result)
        if requirements_content:
            with open(os.path.join(project_dir, 'requirements.txt'), 'w') as f:
                f.write(requirements_content)
            print(f"📄 Saved: requirements.txt")
        
        # If no Python code was extracted, create a basic implementation
        if not os.path.exists(os.path.join(project_dir, 'main.py')):
            self._create_basic_implementation(project_dir, result)
    
    def _extract_python_code(self, result: str) -> str:
        """Extract Python code from the agent output"""
        lines = result.split('\n')
        in_python_block = False
        python_code = []
        
        for line in lines:
            if '```python' in line:
                in_python_block = True
                continue
            elif '```' in line and in_python_block:
                in_python_block = False
                break
            elif in_python_block:
                python_code.append(line)
        
        return '\n'.join(python_code) if python_code else ""
    
    def _extract_readme_content(self, result: str) -> str:
        """Extract README content from the agent output"""
        lines = result.split('\n')
        in_markdown_block = False
        readme_content = []
        
        for line in lines:
            if '```markdown' in line:
                in_markdown_block = True
                continue
            elif '```' in line and in_markdown_block:
                in_markdown_block = False
                break
            elif in_markdown_block:
                readme_content.append(line)
        
        return '\n'.join(readme_content) if readme_content else ""
    
    def _extract_requirements_content(self, result: str) -> str:
        """Extract requirements.txt content from the agent output"""
        lines = result.split('\n')
        in_requirements_block = False
        requirements_content = []
        
        for line in lines:
            if '```text' in line and 'requirements' in line.lower():
                in_requirements_block = True
                continue
            elif '```' in line and in_requirements_block:
                in_requirements_block = False
                break
            elif in_requirements_block:
                requirements_content.append(line)
        
        return '\n'.join(requirements_content) if requirements_content else ""
    
    def _create_basic_implementation(self, project_dir: str, result: str):
        """Create a basic implementation if no code was extracted"""
        # Extract project name from directory
        project_name = os.path.basename(project_dir)
        
        # Create a basic Python implementation
        basic_code = f'''"""
{project_name} - Basic Implementation
Generated by Multi-Agent Software Development System
"""

def main():
    """Main function for {project_name}"""
    print(f"Welcome to {{project_name}}!")
    print("This is a basic implementation generated by the Multi-Agent System.")
    print("Please review the requirements and implement the full functionality.")
    
    # TODO: Implement the actual functionality based on requirements
    # TODO: Add proper error handling
    # TODO: Add input validation
    # TODO: Add comprehensive documentation
    
    return True

if __name__ == "__main__":
    main()
'''
        
        with open(os.path.join(project_dir, 'main.py'), 'w') as f:
            f.write(basic_code)
        
        print(f"📄 Created basic implementation: main.py")
        
        # Create a requirements.txt if it doesn't exist
        requirements_file = os.path.join(project_dir, 'requirements.txt')
        if not os.path.exists(requirements_file):
            with open(requirements_file, 'w') as f:
                f.write("# Basic requirements for the project\n")
                f.write("# Add specific dependencies as needed\n")
            print(f"📄 Created: requirements.txt")
    
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
    
    def delete_project(self, project_name: str) -> bool:
        """Delete a project from the file system"""
        project_dir = os.path.join(self.output_dir, project_name)
        
        if not os.path.exists(project_dir):
            raise FileNotFoundError(f"Project '{project_name}' not found")
        
        try:
            # Remove the entire project directory and all its contents
            import shutil
            shutil.rmtree(project_dir)
            print(f"🗑️ Deleted project: {project_name}")
            return True
        except Exception as e:
            print(f"❌ Error deleting project {project_name}: {e}")
            return False 