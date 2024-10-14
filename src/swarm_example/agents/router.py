# src/swarm_example/agents/router.py

import os
from swarm import Agent
from .brainstormer import brainstormer_agent
from .editor import editor_agent
from .programmer import programmer_agent

def transfer_to_brainstormer():
    return brainstormer_agent

def transfer_to_editor():
    return editor_agent

def transfer_to_programmer():
    return programmer_agent

agent_dir = os.path.dirname(__file__)
instructions_file = os.path.join(agent_dir, 'router_instructions.md')

router_agent = Agent(
    name="Router Agent",
    instructions=open(instructions_file, 'r', encoding='utf-8').read(),
    functions=[transfer_to_brainstormer, transfer_to_editor, transfer_to_programmer],
    llm_config={
        "model": "gpt-4o-mini",
        "temperature": 0.0,  # Ensure deterministic output
        "max_tokens": 20,
    },
)
