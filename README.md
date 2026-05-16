# Lexi-AI 🤖

**Created by dfw-ghost**

Lexi-AI is a fast-thinking artificial intelligence assistant designed to help with code generation, app simulation, and intelligent problem-solving. Built with simplicity and power in mind for developers of all levels.

## Features

- ⚡ **Fast Thinking** - Quick response generation and reasoning
- 💻 **Code Generation** - Generate code snippets in multiple languages
- 🎮 **App Simulation** - Simulate application behavior and workflows
- 🔧 **Easy to Use** - Simple CLI interface for quick interactions
- 🎯 **Extensible** - Easy to add new features and capabilities
- 🌐 **API Integration Ready** - Connect to multiple AI providers

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- API key from supported AI provider (OpenAI, Anthropic, or Hugging Face)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/theunknownghost6578-dev/lexi-ai.git
   cd lexi-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your configuration**
   ```bash
   cp config.example.json config.json
   ```
   Then edit `config.json` and add your API key.

5. **Run Lexi-AI**
   ```bash
   python main.py
   ```

## Usage

### Interactive Mode
```bash
python main.py
```

Then type your queries:
```
Lexi-AI> Generate a Python function to calculate fibonacci numbers
Lexi-AI> Create a React component for a login form
Lexi-AI> Simulate a REST API call
Lexi-AI> exit
```

### Command Line Mode
```bash
python main.py --query "Generate a Python hello world program"
python main.py --code "function" --language "javascript"
python main.py --simulate "api"
```

## Configuration

Edit `config.json` to customize:

```json
{
  "ai_provider": "openai",
  "api_key": "your-api-key-here",
  "model": "gpt-4",
  "temperature": 0.7,
  "max_tokens": 2000,
  "app_name": "Lexi-AI",
  "creator": "dfw-ghost"
}
```

### Supported Providers
- **OpenAI** - GPT-4, GPT-3.5-turbo
- **Anthropic** - Claude
- **Hugging Face** - Open source models

## Project Structure

```
lexi-ai/
├── main.py                 # Main application entry point
├── config.json            # Configuration file (create from example)
├── config.example.json    # Example configuration
├── requirements.txt       # Python dependencies
├── lexi/
│   ├── __init__.py
│   ├── ai_core.py        # Core AI logic
│   ├── code_generator.py # Code generation module
│   ├── app_simulator.py  # App simulation module
│   └── utils.py          # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_lexi.py      # Unit tests
├── examples/
│   ├── code_examples.py
│   └── usage_examples.py
├── README.md             # This file
├── SETUP.md              # Detailed setup guide
├── LICENSE               # MIT License
└── .gitignore           # Git ignore rules
```

## Examples

### Generate Code
```bash
python main.py --query "Write a function to validate email addresses in Python"
```

### Simulate Application
```bash
python main.py --simulate "ecommerce_checkout"
```

### Interactive Session
```bash
python main.py
Lexi-AI> What's the difference between async and await in JavaScript?
Lexi-AI> Generate a database schema for a blog application
Lexi-AI> Show me REST API best practices
Lexi-AI> exit
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Adding New Features
1. Create a new module in the `lexi/` directory
2. Add your feature logic
3. Import and integrate in `main.py`
4. Add tests in `tests/`
5. Update this README

## Troubleshooting

### Issue: "API key not found"
**Solution:** Make sure your `config.json` file exists and contains a valid API key.

### Issue: "Module not found"
**Solution:** Run `pip install -r requirements.txt` to install all dependencies.

### Issue: "Connection timeout"
**Solution:** Check your internet connection and API provider status.

## System Requirements

- **OS:** Windows, macOS, Linux
- **RAM:** Minimum 4GB recommended
- **Storage:** ~500MB for dependencies
- **Internet:** Required for API calls

## API Provider Comparison

| Provider | Speed | Cost | Quality |
|----------|-------|------|---------|
| OpenAI (GPT-4) | Medium | High | Excellent |
| OpenAI (GPT-3.5) | Fast | Low | Very Good |
| Anthropic (Claude) | Medium | Medium | Excellent |
| Hugging Face | Variable | Free/Low | Good |

## Roadmap

- [ ] Web UI interface
- [ ] Multi-language support
- [ ] Local model support
- [ ] Conversation history
- [ ] Code execution environment
- [ ] Plugin system
- [ ] Docker containerization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions:
1. Check existing [GitHub Issues](https://github.com/theunknownghost6578-dev/lexi-ai/issues)
2. Create a new issue with details
3. Join our community discussions

## Credits

**Created by: dfw-ghost**

Built with ❤️ for the developer community.

## Disclaimer

Lexi-AI is a tool designed to assist developers. Always review generated code for security and correctness. The creators are not responsible for the output generated or how it's used.

---

**Happy coding! 🚀**
