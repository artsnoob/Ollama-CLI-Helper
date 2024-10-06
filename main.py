import sys
import requests
from rich import print as rprint
from rich.panel import Panel
from rich.markdown import Markdown

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Function to query Ollama
def query_ollama(prompt):
    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()['response']
    else:
        return f"Error: Unable to get response from Ollama. Status code: {response.status_code}"

# Main function
def main():
    if len(sys.argv) < 2:
        rprint("[bold red]Usage:[/bold red] python3 main.py <your query>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    prompt = f"I'm looking for information about this terminal command on MacOS: {query}. Can you explain what it does and provide an example of how to use it? Format your response in markdown, using code blocks for commands and examples. Keep the answer short and concise."

    rprint("[bold blue]Thinking...[/bold blue]")
    response = query_ollama(prompt)

    rprint("\n[bold green]Here's what I found:[/bold green]\n")
    rprint(Panel(Markdown(response), expand=False, border_style="green"))

if __name__ == "__main__":
    main()
