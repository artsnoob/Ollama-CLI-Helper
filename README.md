# Ollama CLI Helper

This Python script provides a command-line interface to query the Ollama API for information about MacOS terminal commands. It uses the `llama3.2` model to generate explanations and examples for the provided commands.

## Features

- Query Ollama API for MacOS terminal command information
- Format responses in Markdown
- Rich console output for better readability

## Requirements

- Python 3.x
- `requests` library
- `rich` library
- Ollama running locally on port 11434

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:

```bash
pip install requests rich
```

3. Ensure Ollama is running locally on the default port (11434).

## Add script to the ZSH config for easy access.


Open your zsh config file:

```bash
nano ~/.zshrc
```

Add the following line to create an alias (adjust the path to where your script is located):

```bash
alias h='python3 /path/to/your/script/main.py'
```

Save the file and exit nano (Ctrl+X, then Y, then Enter).
Reload your zsh configuration:

```bash
source ~/.zshrc
```

Now you can use the alias to query the app. For example:

```bash
h ls -la
```

This will run your script and provide an explanation for the ls -la command.
You can replace ls -la with any other command you want to learn about. The app will query Ollama and return the explanation in a formatted output.
Would you like me to clarify or expand on any part of this explanation?

## How it works

1. The script takes your query as command-line arguments.
2. It sends a request to the Ollama API, asking for an explanation of the provided command.
3. The response is formatted in Markdown and displayed in a rich panel for better readability.

## Customization

You can modify the `OLLAMA_API_URL` variable if your Ollama instance is running on a different port or host.

## Error Handling

If you don't provide a query, the script will display a usage message.
If there's an error connecting to the Ollama API, an error message will be displayed.
