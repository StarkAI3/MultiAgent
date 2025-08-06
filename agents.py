"""
Agent definitions for the Multi-Agent Software Development System
"""
from crewai import Agent
from langchain_community.llms import Ollama
from config import Config

class AgentFactory:
    """Factory class for creating agents"""
    
    def __init__(self):
        """Initialize the agent factory with Ollama model"""
        # Use the correct format for Ollama with LiteLLM
        self.llm = Ollama(
            model="ollama/gemma3:latest",
            base_url=Config.OLLAMA_BASE_URL,
            temperature=0.1
        )
    
    def create_software_developer_agent(self) -> Agent:
        """Create the Software Developer Agent"""
        config = Config.AGENT_CONFIGS["software_developer"]
        
        return Agent(
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
            llm=self.llm,
            verbose=config["verbose"],
            allow_delegation=config["allow_delegation"],
            memory=True
        )
    
    def create_code_reviewer_agent(self) -> Agent:
        """Create the Code Reviewer Agent"""
        config = Config.AGENT_CONFIGS["code_reviewer"]
        
        return Agent(
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
            llm=self.llm,
            verbose=config["verbose"],
            allow_delegation=config["allow_delegation"],
            memory=True
        ) 