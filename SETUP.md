# Lexi-AI Setup Guide

**Created by dfw-ghost**

This guide will help you set up Lexi-AI step by step.

## Step 1: Prerequisites

Before starting, make sure you have:

- **Python 3.8+** installed ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Git** installed ([Download](https://git-scm.com/))
- An API key from one of the supported providers

## Step 2: Get an API Key

Choose ONE provider and get your API key:

### Option A: OpenAI (Recommended for beginners)
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Click **API keys** in the left sidebar
4. Click **Create new secret key**
5. Copy the key (save it somewhere safe)
6. Add credits to your account (you get $5 free trial)

### Option B: Anthropic (Claude)
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Click **API keys**
4. Click **Create Key**
5. Copy the key

### Option C: Hugging Face (Free, open-source)
1. Go to [huggingface.co](https://huggingface.co)
2. Sign up or log in
3. Click your profile → Settings
4. Click **Access Tokens**
5. Create a new token with `read` access

## Step 3: Clone the Repository

Open terminal/command prompt and run:

```bash
git clone https://github.com/theunknownghost6578-dev/lexi-ai.git
cd lexi-ai
```

## Step 4: Create Virtual Environment

A virtual environment keeps your project dependencies isolated.

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required Python packages. Wait for it to complete.

## Step 6: Configure Your API Key

### Create your config file:
```bash
cp config.example.json config.json
```

### Edit `config.json`:

**On Windows (Notepad):**
```bash
notepad config.json
```

**On macOS/Linux (nano editor):**
```bash
nano config.json
```

Replace the values:

```json
{
  "ai_provider": "openai",
  "api_key": "sk-YOUR-API-KEY-HERE",
  "model": "gpt-4",
  "temperature": 0.7,
  "max_tokens": 2000,
  "app_name": "Lexi-AI",
  "creator": "dfw-ghost"
}
```

**Important settings:**
- `ai_provider`: `"openai"`, `"anthropic"`, or `"huggingface"`
- `api_key`: Your actual API key from the provider
- `model`: 
  - For OpenAI: `"gpt-4"` or `"gpt-3.5-turbo"`
  - For Anthropic: `"claude-3-opus-20240229"`
  - For Hugging Face: `"meta-llama/Llama-2-7b-chat-hf"`
- `temperature`: 0.0 (deterministic) to 1.0 (creative)

Save the file:
- **Notepad:** Ctrl+S
- **Nano:** Ctrl+X, then Y, then Enter

## Step 7: Test the Installation

### Run Lexi-AI in interactive mode:

```bash
python main.py
```

You should see:
```
╔═══════════════════════════════════════╗
║     Lexi-AI v1.0.0                   ║
║     Created by dfw-ghost             ║
╚═══════════════════════════════════════╝

Type 'help' for commands or 'exit' to quit.

Lexi-AI>
```

Try typing:
```
Lexi-AI> Hello, how are you?
```

If it responds, **congratulations!** ✅ You're all set!

## Step 8: Try Some Commands

### Code Generation:
```
Lexi-AI> Generate a Python function to check if a number is prime
```

### Asking Questions:
```
Lexi-AI> What is machine learning?
```

### Code Optimization:
```
Lexi-AI> code: optimize this loop for better performance
```

### App Simulation:
```
Lexi-AI> simulate: User creates account and makes a purchase
```

### Get Help:
```
Lexi-AI> help
```

## Command Line Usage (Alternative)

Instead of interactive mode, you can use commands directly:

```bash
# Ask a question
python main.py --query "How do I create a REST API?"

# Generate code
python main.py --code "function" --language "python"

# Simulate an app flow
python main.py --simulate "login"

# Get help
python main.py --help
```

## Troubleshooting

### Error: "ModuleNotFoundError"
**Solution:** Make sure you activated the virtual environment:
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### Error: "API key not found" or "Invalid API key"
**Solution:**
1. Check that `config.json` exists
2. Make sure your API key is correct (copy from provider again)
3. Make sure you're using the right provider name
4. Check that your account has credits/balance

### Error: "Connection timeout"
**Solution:**
1. Check your internet connection
2. Check that the AI provider is online (check their status page)
3. Increase timeout in `config.json`: change `"timeout": 30` to `60`

### Error: "rate_limit_exceeded"
**Solution:** You've hit API rate limits. Wait a few minutes before trying again, or upgrade your API plan.

### Nothing happens after I type a command
**Solution:**
1. The AI is thinking - wait a bit (it usually takes 5-30 seconds)
2. Check your API key and internet connection
3. Look at the terminal for any error messages

## Next Steps

1. **Explore the code** - Check out the `lexi/` folder to understand the architecture
2. **Run tests** - `python -m pytest tests/`
3. **Create examples** - Try different prompts and save useful ones
4. **Customize** - Edit `config.json` to adjust behavior
5. **Extend** - Add new modules to the `lexi/` folder for custom features

## Performance Tips

- Use GPT-3.5-turbo for faster, cheaper responses
- Set `temperature` lower (0.3-0.5) for consistent outputs
- Set `temperature` higher (0.8-1.0) for creative outputs
- Reduce `max_tokens` if responses are too long
- Add more details to your prompts for better results

## Getting Help

1. **Check the README.md** - General information
2. **Look at examples/** - See how to use features
3. **Check GitHub issues** - See if others had the same problem
4. **Create a GitHub issue** - Ask the community

## Uninstalling

If you want to remove Lexi-AI:

```bash
cd ..  # Go up one directory
rm -rf lexi-ai  # Remove the folder
```

The virtual environment `venv` folder can also be deleted.

---

**You're all set! Start building amazing things with Lexi-AI! 🚀**
