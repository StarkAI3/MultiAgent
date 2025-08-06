"""
Main entry point for the Multi-Agent Software Development System
"""
import argparse
import sys
from multi_agent_system import MultiAgentSystem

def main():
    """Main function with CLI interface"""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Software Development System using Gemma3:latest"
    )
    
    parser.add_argument(
        "--create-project",
        type=str,
        help="Create a new project with the given requirements"
    )
    
    parser.add_argument(
        "--project-name",
        type=str,
        help="Name for the project (optional)"
    )
    
    parser.add_argument(
        "--list-projects",
        action="store_true",
        help="List all completed projects"
    )
    
    parser.add_argument(
        "--show-project",
        type=str,
        help="Show details of a specific project"
    )
    
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run an example project"
    )
    
    args = parser.parse_args()
    
    # Initialize the multi-agent system
    try:
        mas = MultiAgentSystem()
        print("🤖 Multi-Agent System initialized successfully!")
        print(f"📦 Using model: {mas.agent_factory.llm.model}")
    except Exception as e:
        print(f"❌ Error initializing system: {e}")
        print("💡 Make sure Ollama is running and gemma3:latest is installed")
        sys.exit(1)
    
    # Handle different commands
    if args.create_project:
        print("\n" + "="*50)
        print("🚀 CREATING NEW PROJECT")
        print("="*50)
        
        result = mas.create_project(args.create_project, args.project_name)
        print(f"\n✅ Project created successfully!")
        print(f"📁 Project directory: {result['project_dir']}")
        
    elif args.list_projects:
        print("\n" + "="*50)
        print("📋 COMPLETED PROJECTS")
        print("="*50)
        
        projects = mas.list_projects()
        if not projects:
            print("No completed projects found.")
        else:
            for i, project in enumerate(projects, 1):
                print(f"\n{i}. {project['project_name']}")
                print(f"   📅 Created: {project['timestamp']}")
                print(f"   🤖 Model: {project['model_used']}")
                print(f"   📝 Requirements: {project['requirements'][:100]}...")
                
    elif args.show_project:
        print("\n" + "="*50)
        print(f"📖 PROJECT DETAILS: {args.show_project}")
        print("="*50)
        
        try:
            details = mas.get_project_details(args.show_project)
            print(f"\n📅 Created: {details['metadata']['timestamp']}")
            print(f"🤖 Model: {details['metadata']['model_used']}")
            print(f"👥 Agents: {', '.join(details['metadata']['agents'])}")
            print(f"\n📋 Requirements:")
            print(details['metadata']['requirements'])
            print(f"\n📄 Result:")
            print(details['result'])
        except FileNotFoundError:
            print(f"❌ Project '{args.show_project}' not found")
            
    elif args.example:
        print("\n" + "="*50)
        print("🎯 RUNNING EXAMPLE PROJECT")
        print("="*50)
        
        example_requirements = """
        Create a Python web application with the following features:
        1. RESTful API for user management (CRUD operations)
        2. User authentication with JWT tokens
        3. Database integration (SQLite for simplicity)
        4. Input validation and error handling
        5. API documentation
        6. Unit tests
        7. Docker configuration
        
        The application should follow best practices for:
        - Code organization and structure
        - Security (input validation, SQL injection prevention)
        - Performance optimization
        - Error handling and logging
        - Documentation
        """
        
        result = mas.create_project(example_requirements, "example_user_management_api")
        print(f"\n✅ Example project completed!")
        print(f"📁 Project directory: {result['project_dir']}")
        
    else:
        # Show help if no arguments provided
        parser.print_help()
        print("\n" + "="*50)
        print("💡 QUICK START")
        print("="*50)
        print("1. Run an example: python main.py --example")
        print("2. Create a project: python main.py --create-project 'Your requirements here'")
        print("3. List projects: python main.py --list-projects")
        print("4. Show project details: python main.py --show-project project_name")

if __name__ == "__main__":
    main() 