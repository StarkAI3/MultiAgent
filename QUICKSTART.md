# Quick Start Guide

Get your Multi-Agent Software Development System up and running in minutes!

## 🚀 5-Minute Setup

### 1. Prerequisites Check

Make sure you have:

-   Python 3.8+ installed
-   At least 16GB RAM (32GB recommended)
-   Ollama installed and running

### 2. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Gemma3:latest model (if not already installed)
ollama pull gemma3:latest
```

### 3. Test the System

```bash
# Run the test suite
python test_system.py

# Or run an example project
python main.py --example
```

### 4. Create Your First Project

```bash
# Create a simple project
python main.py --create-project "Create a Python web scraper that extracts data from a website and saves it to a CSV file"
```

## 🎯 Common Use Cases

### Web Development

```bash
python main.py --create-project "Build a Flask web application for a todo list with user authentication, database storage, and REST API endpoints"
```

### Data Science

```bash
python main.py --create-project "Create a machine learning pipeline that loads data from CSV, preprocesses it, trains a model, and provides prediction endpoints"
```

### API Development

```bash
python main.py --create-project "Develop a FastAPI application for a weather service that fetches data from external APIs and provides caching"
```

### Automation Scripts

```bash
python main.py --create-project "Write a Python script that monitors system resources, logs the data, and sends alerts when thresholds are exceeded"
```

## 🔧 Troubleshooting

### Ollama Issues

```bash
# Check if Ollama is running
ollama list

# Start Ollama if not running
ollama serve

# Check available models
ollama list
```

### Model Issues

```bash
# Pull the model again
ollama pull gemma3:latest

# Check model status
ollama show gemma3:latest
```

### Python Issues

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📊 System Requirements

| Component | Minimum | Recommended |
| --------- | ------- | ----------- |
| RAM       | 16GB    | 32GB+       |
| GPU VRAM  | 8GB     | 12GB+       |
| Storage   | 50GB    | 100GB+      |
| Python    | 3.8     | 3.9+        |

## 🎨 Example Output

When you run a project, you'll see:

```
🚀 Starting project: example_user_management_api
📋 Requirements: Create a Python web application with the following features...
🔄 Executing multi-agent workflow...

🤖 Software Developer Agent: Analyzing requirements...
🤖 Software Developer Agent: Designing architecture...
🤖 Software Developer Agent: Writing code...
🤖 Code Reviewer Agent: Reviewing code quality...
🤖 Code Reviewer Agent: Checking security...
🤖 Code Reviewer Agent: Providing feedback...

✅ Project completed: example_user_management_api
📁 Project directory: output/example_user_management_api
```

## 📁 Project Structure

Generated projects include:

-   Complete source code
-   Documentation (README.md)
-   Unit tests
-   Configuration files
-   Docker setup (if applicable)
-   API documentation

## 🔍 Viewing Results

```bash
# List all projects
python main.py --list-projects

# View specific project details
python main.py --show-project project_name

# Navigate to project directory
cd output/project_name
ls -la
```

## 🚨 Common Errors

1. **"Ollama connection failed"**

    - Make sure Ollama is running: `ollama serve`

2. **"Model not found"**

    - Install the model: `ollama pull gemma3:latest`

3. **"Memory error"**

    - Close other applications
    - Use a smaller model variant
    - Increase system RAM

4. **"Import error"**
    - Install dependencies: `pip install -r requirements.txt`

## 🎯 Next Steps

1. **Explore Examples**: Run `python main.py --example`
2. **Create Custom Projects**: Use your own requirements
3. **Customize Agents**: Modify `config.py` for different behaviors
4. **Add More Agents**: Extend the system with additional specialized agents
5. **Integrate with IDEs**: Use the generated code in your development workflow

## 📞 Need Help?

-   Check the main README.md for detailed documentation
-   Review the troubleshooting section
-   Check the example projects in the `output/` directory
-   Open an issue on GitHub

---

**Happy coding with your AI development team! 🚀**
