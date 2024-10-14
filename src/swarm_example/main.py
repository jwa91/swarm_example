# src/swarm_example/main.py

import os
from swarm import Swarm
from .agents.router import router_agent
from dotenv import load_dotenv

def main():
    load_dotenv()
    client = Swarm()

    # Simulate user queries
    user_messages = [
        "I need some ideas for a new mobile app.",
        "Can you edit this paragraph for me? The quick brown fox jumps over the lazy dog.",
        "How do I write a function in Python?",
    ]

    for message in user_messages:
        print(f"\nUser: {message}")
        # Start with the router agent
        response = client.run(
            agent=router_agent,
            messages=[{"role": "user", "content": message}],
            debug=True,  # Enable debug output
        )
        # Print verbose output
        for msg in response.messages:
            role = msg['role'].capitalize()
            sender = msg.get('sender', 'Unknown')
            content = msg['content']
            if role == 'Assistant':
                print(f"Assistant ({sender}): {content}")
            elif role == 'Function':
                print(f"Function Call: {msg['name']} with arguments {msg['arguments']}")
            elif role == 'Tool_response':
                print(f"Function Response: {content}")
            elif role == 'User':
                print(f"User: {content}")
            # Skip 'System' messages
        # Show the assistant's name
        print(f"Assistant Name: {response.agent.name}")

if __name__ == "__main__":
    main()
