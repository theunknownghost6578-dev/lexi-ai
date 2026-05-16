"""
Lexi-AI Core Module
Created by dfw-ghost
Main AI engine that handles all interactions with LLM providers
"""

import json
import os
from typing import Optional


class AICore:
    """Core AI engine for Lexi-AI"""
    
    def __init__(self, config_path: str = 'config.json'):
        """Initialize the AI core with configuration"""
        self.config = self.load_config(config_path)
        self.provider = self.config.get('ai_provider', 'openai')
        self.api_key = self.config.get('api_key')
        self.model = self.config.get('model', 'gpt-4')
        self.temperature = self.config.get('temperature', 0.7)
        self.max_tokens = self.config.get('max_tokens', 2000)
        
        # Initialize the appropriate provider
        if self.provider == 'openai':
            try:
                import openai
                openai.api_key = self.api_key
                self.client = openai.ChatCompletion
            except ImportError:
                raise ImportError("OpenAI library not installed. Run: pip install openai")
        else:
            raise ValueError(f"Provider '{self.provider}' not yet implemented")
    
    @staticmethod
    def load_config(config_path: str) -> dict:
        """Load configuration from JSON file"""
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def ask(self, prompt: str) -> str:
        """Send a prompt to the AI and get response"""
        try:
            response = self.client.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are Lexi-AI, a helpful AI assistant created by dfw-ghost. You are expert at code generation, app simulation, and technical problem-solving. Provide clear, practical, and well-formatted responses."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"
    
    def code_generate(self, description: str) -> str:
        """Generate code based on description"""
        prompt = f"Generate clean, production-ready code for: {description}"
        return self.ask(prompt)
    
    def simulate_app(self, scenario: str) -> str:
        """Simulate an application flow"""
        prompt = f"Simulate a detailed step-by-step flow for: {scenario}. Include all interactions and possible outcomes."
        return self.ask(prompt)
    
    def optimize_code(self, code: str) -> str:
        """Optimize code for performance"""
        prompt = f"Optimize this code for performance and readability:\n\n```\n{code}\n```\n\nProvide the optimized version with explanations."
        return self.ask(prompt)
    
    def fix_code(self, code: str, error: str = '') -> str:
        """Fix code issues"""
        if error:
            prompt = f"Fix this code that produces this error: {error}\n\n```\n{code}\n```\n\nProvide the fixed code with explanation."
        else:
            prompt = f"Review and fix any bugs in this code:\n\n```\n{code}\n```"
        return self.ask(prompt)
    
    def explain_code(self, code: str) -> str:
        """Explain what code does"""
        prompt = f"Explain this code in detail:\n\n```\n{code}\n```"
        return self.ask(prompt)
