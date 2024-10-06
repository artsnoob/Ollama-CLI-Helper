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

## Usage

Run the script from the command line, providing the MacOS terminal command you want to learn about:

```bash
python3 main.py <your query>
```

For example:

```bash
python3 main.py ls -la
```

## How it works

1. The script takes your query as command-line arguments.
2. It sends a request to the Ollama API, asking for an explanation of the provided command.
3. The response is formatted in Markdown and displayed in a rich panel for better readability.

## Customization

You can modify the `OLLAMA_API_URL` variable if your Ollama instance is running on a different port or host.

## Error Handling

If you don't provide a query, the script will display a usage message.
If there's an error connecting to the Ollama API, an error message will be displayed.
