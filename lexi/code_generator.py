"""
Lexi-AI Code Generator Module
Created by dfw-ghost
"""

from lexi.ai_core import AICore


class CodeGenerator:
    """Handle code generation in multiple languages"""
    
    SUPPORTED_LANGUAGES = [
        'python', 'javascript', 'typescript', 'java', 'c++', 'c#',
        'go', 'rust', 'php', 'ruby', 'swift', 'kotlin'
    ]
    
    def __init__(self, ai_core: AICore):
        self.ai = ai_core
    
    def generate_code(self, prompt: str, language: str = 'python') -> str:
        """Generate code in specified language"""
        if language.lower() not in self.SUPPORTED_LANGUAGES:
            language = 'python'
        
        full_prompt = f"Generate {language} code for: {prompt}\n\nProvide clean, well-commented, production-ready code."
        return self.ai.ask(full_prompt)
    
    def generate_function(self, description: str, language: str = 'python') -> str:
        """Generate a specific function"""
        prompt = f"Create a {language} function that: {description}\n\nInclude docstring and type hints."
        return self.ai.ask(prompt)
    
    def generate_class(self, description: str, language: str = 'python') -> str:
        """Generate a class/object"""
        prompt = f"Design a {language} class that: {description}\n\nInclude constructor, methods, and documentation."
        return self.ai.ask(prompt)
    
    def optimize_code(self, code: str) -> str:
        """Optimize existing code"""
        prompt = f"Optimize this code for performance and readability:\n\n```\n{code}\n```\n\nExplain the optimizations."
        return self.ai.ask(prompt)
    
    def fix_code(self, code: str, error: str = '') -> str:
        """Fix code errors"""
        if error:
            prompt = f"Fix this code that has this error: {error}\n\n```\n{code}\n```"
        else:
            prompt = f"Review and fix any bugs in this code:\n\n```\n{code}\n```"
        return self.ai.ask(prompt)
    
    def generate_api_endpoint(self, description: str, language: str = 'python') -> str:
        """Generate a REST API endpoint"""
        prompt = f"Create a {language} REST API endpoint for: {description}\n\nInclude request/response models, error handling, and validation."
        return self.ai.ask(prompt)
    
    def generate_database_schema(self, app_name: str, db_type: str = 'sql') -> str:
        """Generate database schema"""
        prompt = f"Design a {db_type} database schema for a {app_name} application.\n\nInclude tables, relationships, and indexes."
        return self.ai.ask(prompt)
    
    def explain_code(self, code: str) -> str:
        """Explain what code does"""
        prompt = f"Explain this code in simple terms:\n\n```\n{code}\n```"
        return self.ai.ask(prompt)
