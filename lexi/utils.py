"""
Lexi-AI Utilities Module
Created by dfw-ghost
Helper functions and utilities
"""

from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)


def print_header():
    """Print Lexi-AI header"""
    header = """
╔════════════════════════════════════════╗
║                                        ║
║         🤖 Lexi-AI v1.0.0 🤖          ║
║      Created by dfw-ghost              ║
║                                        ║
║  Fast Thinking AI Assistant            ║
║  Code Generation & App Simulation      ║
║                                        ║
╚════════════════════════════════════════╝
"""
    print(Fore.CYAN + header + Style.RESET_ALL)


def print_success(message: str):
    """Print success message"""
    print(Fore.GREEN + f"✓ {message}" + Style.RESET_ALL)


def print_error(message: str):
    """Print error message"""
    print(Fore.RED + f"✗ {message}" + Style.RESET_ALL)


def print_info(message: str):
    """Print info message"""
    print(Fore.BLUE + f"ℹ {message}" + Style.RESET_ALL)


def print_warning(message: str):
    """Print warning message"""
    print(Fore.YELLOW + f"⚠ {message}" + Style.RESET_ALL)


def print_section(title: str):
    """Print a section header"""
    print(Fore.CYAN + f"\n--- {title} ---" + Style.RESET_ALL)


def format_response(response: str) -> str:
    """Format AI response for display"""
    return response


def get_command_help():
    """Return help text for commands"""
    return """
╔════════════════════════════════════════╗
║          LEXI-AI COMMANDS              ║
╚════════════════════════════════════════╝

📝 CODE GENERATION:
  code: [description]     - Generate code
  function: [description] - Generate a function
  class: [description]    - Generate a class
  api: [description]      - Generate API endpoint
  optimize: [code]        - Optimize code
  fix: [code]            - Fix code errors
  explain: [code]        - Explain code

🎮 APP SIMULATION:
  simulate: [scenario]    - Simulate app flow
  journey: [description]  - Simulate user journey
  api-call: [endpoint]    - Simulate API call
  db: [operation]         - Simulate database operation
  auth: [type]            - Simulate authentication

❓ GENERAL:
  ask: [question]         - Ask Lexi-AI anything
  help                    - Show this help
  clear                   - Clear screen
  exit                    - Exit program

📌 EXAMPLES:
  code: REST API for user authentication
  function: validate email address in python
  simulate: user signup and email verification
  ask: what is machine learning?

🚀 Start typing commands!
"""


def print_loading():
    """Print loading animation"""
    print(Fore.YELLOW + "⏳ Lexi is thinking..." + Style.RESET_ALL)


def print_response_header():
    """Print response header"""
    print(Fore.CYAN + "\n" + "="*40)
    print("LEXI-AI RESPONSE")
    print("="*40 + Style.RESET_ALL)
