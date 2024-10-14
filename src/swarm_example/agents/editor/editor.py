# src/swarm_example/agents/editor/editor.py

import os
import json
from swarm import Agent
from ..utils import create_agent, save_content
from .editor_tools import get_desired_writing_style

agent_dir = os.path.dirname(__file__)
instructions_file = os.path.join(agent_dir, 'instructions.md')

# Load LLM configuration
config_file = os.path.join(agent_dir, 'editor_configuration.json')
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        llm_config = json.load(f)
else:
    llm_config = {
        "model": "gpt-3.5-turbo-0613",
        "temperature": 0.5,
    }

editor_agent = create_agent(
    name="Editor Agent",
    instructions_file=instructions_file,
    functions=[save_content, get_desired_writing_style],
    llm_config=llm_config,
)
