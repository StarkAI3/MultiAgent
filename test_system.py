#!/usr/bin/env python3
"""
Test script for the Multi-Agent Software Development System
"""
import sys
import os
from multi_agent_system import MultiAgentSystem

def test_system_initialization():
    """Test if the system can be initialized"""
    print("🧪 Testing system initialization...")
    
    try:
        mas = MultiAgentSystem()
        print("✅ System initialized successfully")
        print(f"📦 Using model: {mas.agent_factory.llm.model}")
        return mas
    except Exception as e:
        print(f"❌ System initialization failed: {e}")
        return None

def test_simple_project(mas):
    """Test creating a simple project"""
    print("\n🧪 Testing simple project creation...")
    
    simple_requirements = """
    Create a simple Python calculator application that:
    1. Has basic arithmetic operations (add, subtract, multiply, divide)
    2. Includes input validation
    3. Has a simple command-line interface
    4. Includes error handling for division by zero
    5. Has unit tests
    """
    
    try:
        result = mas.create_project(simple_requirements, "test_calculator")
        print("✅ Simple project created successfully")
        print(f"📁 Project directory: {result['project_dir']}")
        return True
    except Exception as e:
        print(f"❌ Simple project creation failed: {e}")
        return False

def test_project_listing(mas):
    """Test project listing functionality"""
    print("\n🧪 Testing project listing...")
    
    try:
        projects = mas.list_projects()
        print(f"✅ Found {len(projects)} projects")
        for project in projects:
            print(f"   - {project['project_name']}")
        return True
    except Exception as e:
        print(f"❌ Project listing failed: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Multi-Agent System Test Suite")
    print("=" * 40)
    
    # Test system initialization
    mas = test_system_initialization()
    if not mas:
        print("❌ Cannot proceed with tests - system initialization failed")
        sys.exit(1)
    
    # Test simple project creation
    if not test_simple_project(mas):
        print("❌ Simple project test failed")
        sys.exit(1)
    
    # Test project listing
    if not test_project_listing(mas):
        print("❌ Project listing test failed")
        sys.exit(1)
    
    print("\n" + "=" * 40)
    print("✅ All tests passed!")
    print("🎉 Your multi-agent system is working correctly!")
    
    print("\n🎯 Next steps:")
    print("1. Try the example: python main.py --example")
    print("2. Create your own project: python main.py --create-project 'Your requirements'")
    print("3. View help: python main.py --help")

if __name__ == "__main__":
    main() 