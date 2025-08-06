#!/usr/bin/env python3
"""
Interactive Web Frontend for Multi-Agent Software Development System
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_socketio import SocketIO, emit
import os
import json
import threading
import time
from datetime import datetime
from multi_agent_system import MultiAgentSystem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variable to store the multi-agent system
mas = None

def initialize_mas():
    """Initialize the multi-agent system"""
    global mas
    try:
        mas = MultiAgentSystem()
        return True
    except Exception as e:
        print(f"Error initializing MAS: {e}")
        return False

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    """Create a new project page"""
    if request.method == 'POST':
        requirements = request.form.get('requirements')
        project_name = request.form.get('project_name', '')
        
        if not requirements:
            flash('Please provide project requirements', 'error')
            return redirect(url_for('create_project'))
        
        # Start project creation in background
        thread = threading.Thread(target=create_project_background, 
                                args=(requirements, project_name))
        thread.daemon = True
        thread.start()
        
        flash('Project creation started! Check the status below.', 'success')
        return redirect(url_for('projects'))
    
    return render_template('create_project.html')

def create_project_background(requirements, project_name):
    """Background task for project creation"""
    try:
        socketio.emit('project_status', {
            'status': 'started',
            'message': 'Initializing agents...'
        })
        
        result = mas.create_project(requirements, project_name)
        
        socketio.emit('project_status', {
            'status': 'completed',
            'message': f'Project completed: {result["project_name"]}',
            'project_dir': result['project_dir']
        })
        
    except Exception as e:
        socketio.emit('project_status', {
            'status': 'error',
            'message': f'Error: {str(e)}'
        })

@app.route('/projects')
def projects():
    """List all projects"""
    try:
        projects_list = mas.list_projects() if mas else []
        return render_template('projects.html', projects=projects_list)
    except Exception as e:
        flash(f'Error loading projects: {str(e)}', 'error')
        return render_template('projects.html', projects=[])

@app.route('/project/<project_name>')
def project_details(project_name):
    """Show project details"""
    try:
        details = mas.get_project_details(project_name)
        return render_template('project_details.html', 
                             project_name=project_name, 
                             details=details)
    except Exception as e:
        flash(f'Error loading project details: {str(e)}', 'error')
        return redirect(url_for('projects'))

@app.route('/api/projects')
def api_projects():
    """API endpoint to get projects"""
    try:
        projects_list = mas.list_projects() if mas else []
        return jsonify(projects_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/project/<project_name>')
def api_project_details(project_name):
    """API endpoint to get project details"""
    try:
        details = mas.get_project_details(project_name)
        return jsonify(details)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/run-example', methods=['POST'])
def api_run_example():
    """API endpoint to run example project"""
    try:
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
        
        # Start example project creation in background
        thread = threading.Thread(target=create_project_background, 
                                args=(example_requirements, "example_user_management_api"))
        thread.daemon = True
        thread.start()
        
        return jsonify({'success': True, 'message': 'Example project started'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/status')
def status():
    """System status page"""
    status_info = {
        'mas_initialized': mas is not None,
        'model': mas.agent_factory.llm.model if mas else 'Not available',
        'projects_count': len(mas.list_projects()) if mas else 0,
        'workspace_dir': mas.workspace_dir if mas else 'Not available',
        'output_dir': mas.output_dir if mas else 'Not available'
    }
    return render_template('status.html', status=status_info)

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    emit('status', {'message': 'Connected to Multi-Agent System'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('Client disconnected')

if __name__ == '__main__':
    # Initialize the multi-agent system
    if initialize_mas():
        print("✅ Multi-Agent System initialized successfully!")
    else:
        print("❌ Failed to initialize Multi-Agent System")
    
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("🚀 Starting web frontend...")
    print("📱 Open your browser and go to: http://localhost:5000")
    
    socketio.run(app, debug=True, host='0.0.0.0', port=5000) 