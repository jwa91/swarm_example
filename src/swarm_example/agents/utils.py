# src/swarm_example/agents/utils.py

import os
from swarm import Agent

def create_agent(name, instructions_file, functions, llm_config=None):
    # Load instructions from the markdown file
    with open(instructions_file, 'r', encoding='utf-8') as f:
        instructions = f.read()
    return Agent(
        name=name,
        instructions=instructions,
        functions=functions,
        llm_config=llm_config or {},
    )

def save_content(content: str, filename: str) -> str:
    # Save the content as a markdown file
    filepath = os.path.join('output', f"{filename}.md")
    os.makedirs('output', exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Content saved to {filepath}"
