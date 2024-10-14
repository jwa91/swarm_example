# src/swarm_example/agents/programmer/programmer.py

import os
import json
from swarm import Agent
from ..utils import create_agent, save_content
from .programmer_tools import get_coding_conventions_python, get_coding_conventions_typescript

agent_dir = os.path.dirname(__file__)
instructions_file = os.path.join(agent_dir, 'instructions.md')

# Load LLM configuration
config_file = os.path.join(agent_dir, 'programmer_configuration.json')
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        llm_config = json.load(f)
else:
    llm_config = {
        "model": "gpt-3.5-turbo-0613",
        "temperature": 0.3,
    }

programmer_agent = create_agent(
    name="Programmer Agent",
    instructions_file=instructions_file,
    functions=[
        save_content,
        get_coding_conventions_python,
        get_coding_conventions_typescript,
    ],
    llm_config=llm_config,
)
