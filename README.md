# Multi-Agent Software Development System

A powerful multi-agent system for automated software development using **Gemma3:latest** and **CrewAI**. This system features two specialized agents that work together to create high-quality, production-ready code.

## 🤖 Agents

### 1. **Software Developer Agent**
- **Role**: Senior Software Developer
- **Goal**: Write high-quality, efficient, and maintainable code
- **Capabilities**:
  - Code generation and architecture design
  - Best practices implementation
  - Documentation creation
  - Error handling and validation
  - Project structure organization

### 2. **Code Reviewer Agent**
- **Role**: Code Review Specialist
- **Goal**: Ensure code quality, security, and adherence to best practices
- **Capabilities**:
  - Code quality assessment
  - Security vulnerability analysis
  - Performance optimization suggestions
  - Best practices compliance review
  - Architecture evaluation

## 🚀 Features

- **Local Model Support**: Uses Gemma3:latest via Ollama for complete privacy
- **Multi-Agent Collaboration**: Agents work together in a coordinated workflow
- **Comprehensive Tools**: File operations, code interpretation, and directory search
- **Project Management**: Automatic project organization and result tracking
- **CLI Interface**: Easy-to-use command-line interface
- **Example Projects**: Built-in examples to get started quickly

## 📋 Prerequisites

### Hardware Requirements
- **RAM**: 16GB+ (32GB recommended)
- **GPU**: RTX 3060+ or equivalent (12GB+ VRAM recommended)
- **Storage**: 50GB+ free space
- **OS**: macOS, Linux, or Windows

### Software Requirements
- Python 3.8+
- Ollama (for running Gemma3:latest locally)
- Git

## 🛠️ Installation

### 1. Install Ollama
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Install Gemma3:latest
```bash
ollama pull gemma3:latest
```

### 3. Clone and Setup the Project
```bash
git clone <your-repo-url>
cd multiagent_implementation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
# Check if Ollama is running
ollama list

# Test the system
python main.py --example
```

## 🎯 Usage

### Quick Start
```bash
# Run an example project
python main.py --example

# Create a custom project
python main.py --create-project "Create a Python web API for user authentication with JWT tokens"

# List all projects
python main.py --list-projects

# View project details
python main.py --show-project project_name
```

### Advanced Usage

#### 1. Create a Custom Project
```bash
python main.py --create-project "Build a machine learning pipeline for image classification using TensorFlow and Flask" --project-name "ml_image_classifier"
```

#### 2. Programmatic Usage
```python
from multi_agent_system import MultiAgentSystem

# Initialize the system
mas = MultiAgentSystem()

# Create a project
requirements = """
Create a Python application that:
1. Scrapes data from a website
2. Processes and cleans the data
3. Stores it in a database
4. Provides a REST API to query the data
5. Includes unit tests and documentation
"""

result = mas.create_project(requirements, "web_scraper_api")
print(f"Project created: {result['project_dir']}")
```

## 📁 Project Structure

```
multiagent_implementation/
├── config.py              # Configuration settings
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── multi_agent_system.py  # Main orchestrator
├── main.py               # CLI interface
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── workspace/           # Working directory for agents
├── output/              # Generated projects
└── ref_data/            # Research materials
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file to customize settings:

```env
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=gemma3:latest
```

### Model Configuration
Edit `config.py` to adjust model parameters:

```python
@classmethod
def get_model_config(cls) -> Dict[str, Any]:
    return {
        "base_url": cls.OLLAMA_BASE_URL,
        "model": cls.MODEL_NAME,
        "temperature": 0.1,  # Lower for more deterministic code
        "top_p": 0.9,
        "max_tokens": 4096
    }
```

## 🎨 Example Projects

The system comes with built-in examples:

1. **User Management API**: Complete REST API with authentication
2. **Machine Learning Pipeline**: Data processing and ML workflow
3. **Web Scraper**: Data collection and storage system
4. **Microservice Architecture**: Distributed system design

## 🔍 Monitoring and Debugging

### Verbose Output
The system provides detailed logging:
```bash
python main.py --create-project "Your requirements" --verbose
```

### Project Tracking
All projects are automatically tracked with metadata:
- Creation timestamp
- Model used
- Requirements
- Agent interactions
- Generated files

## 🚨 Troubleshooting

### Common Issues

1. **Ollama Connection Error**
   ```bash
   # Check if Ollama is running
   ollama list
   
   # Start Ollama if not running
   ollama serve
   ```

2. **Model Not Found**
   ```bash
   # Pull the model
   ollama pull gemma3:latest
   
   # Check available models
   ollama list
   ```

3. **Memory Issues**
   - Reduce model size or use quantization
   - Close other applications
   - Increase system RAM

4. **Performance Issues**
   - Use GPU acceleration if available
   - Adjust model parameters in config.py
   - Consider using smaller model variants

## 🔒 Security Considerations

- **Local Execution**: All code runs locally, no data sent to external services
- **Sandboxed Environment**: Code execution is isolated
- **Input Validation**: All inputs are validated before processing
- **File Permissions**: Generated files have appropriate permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **CrewAI**: Multi-agent orchestration framework
- **Ollama**: Local LLM deployment
- **Gemma3**: Google's open-source language model
- **LangChain**: LLM integration framework

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the example projects
3. Open an issue on GitHub
4. Check the CrewAI documentation

---

**Happy coding with your AI development team! 🚀** 