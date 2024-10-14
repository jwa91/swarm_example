# swarm_example

## Overview

swarm_example is an example project showcasing the implementation of a scalable agent-based system using OpenAI's new swarm library. This repository demonstrates a proposed structure for organizing and managing multiple AI agents within a single application.

## Project Structure

```plaintext
src/swarm_example/
├── agents/
│   ├── brainstormer/
│   │   ├── __init__.py
│   │   ├── brainstormer.py
│   │   ├── brainstormer_configuration.json
│   │   └── instructions.md
│   ├── editor/
│   │   ├── __init__.py
│   │   ├── editor.py
│   │   ├── editor_configuration.json
│   │   ├── editor_tools.py
│   │   └── instructions.md
│   ├── programmer/
│   │   ├── __init__.py
│   │   ├── instructions.md
│   │   ├── programmer.py
│   │   ├── programmer_configuration.json
│   │   └── programmer_tools.py
│   ├── router.py
│   ├── router_instructions.md
│   └── utils.py
├── .env
├── main.py
├── pyproject.toml
└── README.md
```

## Features

1. **Multi-Agent System**: The project implements multiple specialized agents (Brainstormer, Editor, and Programmer) to handle different types of tasks.

2. **Router Agent**: A central Router Agent that analyzes user input and directs the query to the most appropriate specialized agent.

3. **Modular Design**: Each agent is encapsulated in its own directory with specific configurations and instructions.

4. **Flexible Configuration**: JSON configuration files for each agent allow easy customization of LLM parameters.

5. **Utility Functions**: Common functionalities are abstracted into utility functions for code reusability.

6. **Environment Variable Support**: Uses python-dotenv for managing environment variables.

7. **Markdown Instructions**: Agent instructions are stored in separate markdown files for better readability and maintenance.

## Agents

### Router Agent

- **Purpose**: Analyzes user input and directs the query to the appropriate specialized agent.
- **File**: `router.py`
- **Instructions**: `router_instructions.md`

### Brainstormer Agent

- **Purpose**: Generates creative ideas on any given topic.
- **Files**: `brainstormer.py`, `brainstormer_configuration.json`, `instructions.md`
- **Key Feature**: Saves generated ideas to a markdown file.

### Editor Agent

- **Purpose**: Proofreads and improves text, focusing on grammar, clarity, and style.
- **Files**: `editor.py`, `editor_configuration.json`, `editor_tools.py`, `instructions.md`
- **Key Feature**: Applies a specified writing style (e.g., "Write like a pirate").

### Programmer Agent

- **Purpose**: Provides programming assistance, including code snippets and explanations.
- **Files**: `programmer.py`, `programmer_configuration.json`, `programmer_tools.py`, `instructions.md`
- **Key Feature**: Adheres to specified coding conventions for Python and TypeScript.

## Setup and Installation

1. Ensure you have Python 3.10 or higher installed.
2. Clone this repository:

   ```shell
   git clone https://github.com/your-username/swarm_example.git
   cd swarm_example
   ```

3. Install the project and its dependencies:

   ```shell
   pip install -e .
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the main script to see the multi-agent system in action:

```shell
python -m swarm_example.main
```

This will simulate user queries and demonstrate how the Router Agent directs them to the appropriate specialized agent.

## Customization

- Modify the JSON configuration files in each agent's directory to adjust LLM parameters.
- Edit the markdown instruction files to change agent behaviors.
- Add new agents by creating a new directory under `agents/` and following the existing structure.

## Dependencies

- python-dotenv
- openai
- swarm (from OpenAI's GitHub repository)
