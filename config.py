"""
Configuration file for the Multi-Agent Software Development System
"""
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the multi-agent system"""
    
    # Ollama Configuration
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:latest")
    
    # Agent Configuration
    AGENT_CONFIGS = {
        "software_developer": {
            "role": "Senior Software Developer",
            "goal": "Write high-quality, efficient, and maintainable code following best practices",
            "backstory": """You are a senior software engineer with 10+ years of experience 
                          across multiple programming languages and frameworks. You excel at 
                          architectural decisions, clean code principles, and creating scalable 
                          solutions. You always write well-documented, production-ready code.""",
            "verbose": True,
            "allow_delegation": False
        },
        "code_reviewer": {
            "role": "Code Review Specialist", 
            "goal": "Ensure code quality, security, and adherence to best practices",
            "backstory": """You are a meticulous code reviewer with expertise in multiple 
                          programming languages, security vulnerabilities, and software 
                          architecture patterns. You focus on maintainability, performance, 
                          and code quality. You provide constructive feedback and suggest 
                          improvements.""",
            "verbose": True,
            "allow_delegation": False
        }
    }
    
    # Task Configuration
    TASK_CONFIGS = {
        "development": {
            "description": "Develop high-quality, production-ready code based on requirements",
            "expected_output": "Complete, well-documented code with proper structure and error handling"
        },
        "review": {
            "description": "Review code for quality, security, and best practices",
            "expected_output": "Detailed code review with specific suggestions and improvements"
        }
    }
    
    # File paths
    WORKSPACE_DIR = "workspace"
    OUTPUT_DIR = "output"
    
    @classmethod
    def get_model_config(cls) -> Dict[str, Any]:
        """Get model configuration for Ollama"""
        return {
            "base_url": cls.OLLAMA_BASE_URL,
            "model": cls.MODEL_NAME,
            "temperature": 0.1  # Lower temperature for more deterministic code generation
        } 