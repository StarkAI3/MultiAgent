#!/usr/bin/env python3
"""
Setup script for the Multi-Agent Software Development System
"""
import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_ollama():
    """Check if Ollama is installed and running"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Ollama is installed and running")
            return True
        else:
            print("❌ Ollama is not running")
            return False
    except FileNotFoundError:
        print("❌ Ollama is not installed")
        return False

def install_ollama():
    """Install Ollama"""
    system = platform.system().lower()
    
    if system == "darwin":  # macOS
        print("📦 Installing Ollama on macOS...")
        subprocess.run(['curl', '-fsSL', 'https://ollama.ai/install.sh', '|', 'sh'])
    elif system == "linux":
        print("📦 Installing Ollama on Linux...")
        subprocess.run(['curl', '-fsSL', 'https://ollama.ai/install.sh', '|', 'sh'])
    elif system == "windows":
        print("📦 Please install Ollama manually from https://ollama.ai/download")
        return False
    else:
        print(f"❌ Unsupported operating system: {system}")
        return False
    
    return True

def check_gemma_model():
    """Check if Gemma3:latest model is available"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if 'gemma3:latest' in result.stdout:
            print("✅ Gemma3:latest model is available")
            return True
        else:
            print("❌ Gemma3:latest model not found")
            return False
    except:
        return False

def install_gemma_model():
    """Install Gemma3:latest model"""
    print("📦 Installing Gemma3:latest model...")
    print("⚠️  This may take a while depending on your internet connection")
    
    try:
        subprocess.run(['ollama', 'pull', 'gemma3:latest'], check=True)
        print("✅ Gemma3:latest model installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Gemma3:latest model")
        return False

def install_python_dependencies():
    """Install Python dependencies"""
    print("📦 Installing Python dependencies...")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        print("✅ Python dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python dependencies")
        return False

def create_directories():
    """Create necessary directories"""
    directories = ['workspace', 'output']
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def main():
    """Main setup function"""
    print("🚀 Multi-Agent Software Development System Setup")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check/Install Ollama
    if not check_ollama():
        print("\n📦 Installing Ollama...")
        if not install_ollama():
            print("❌ Failed to install Ollama. Please install manually.")
            sys.exit(1)
    
    # Check/Install Gemma3:latest model
    if not check_gemma_model():
        print("\n📦 Installing Gemma3:latest model...")
        if not install_gemma_model():
            print("❌ Failed to install Gemma3:latest model")
            sys.exit(1)
    
    # Install Python dependencies
    print("\n📦 Installing Python dependencies...")
    if not install_python_dependencies():
        print("❌ Failed to install Python dependencies")
        sys.exit(1)
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n🎯 Next steps:")
    print("1. Test the system: python main.py --example")
    print("2. Create a project: python main.py --create-project 'Your requirements'")
    print("3. View help: python main.py --help")
    
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main() 