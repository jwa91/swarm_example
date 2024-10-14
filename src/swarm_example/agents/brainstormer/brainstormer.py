# src/swarm_example/agents/brainstormer/brainstormer.py

import os
import json
from swarm import Agent
from ..utils import create_agent, save_content

agent_dir = os.path.dirname(__file__)
instructions_file = os.path.join(agent_dir, 'instructions.md')

# Load LLM configuration
config_file = os.path.join(agent_dir, 'brainstormer_configuration.json')
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        llm_config = json.load(f)
else:
    llm_config = {
        "model": "gpt-3.5-turbo-0613",
        "temperature": 0.7,
    }

brainstormer_agent = create_agent(
    name="Brainstormer Agent",
    instructions_file=instructions_file,
    functions=[save_content],
    llm_config=llm_config,
)
