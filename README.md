# dynamic_ha_presence

**dynamic_ha_presence** is a modular, Docker-based project that integrates multiple autonomous agents for Home Assistant. The project currently consists of:

- **ble_presence_agent:**
  Detects BLE devices to determine room presence and maps device signals to occupant IDs.
- **behavior_agent:**
  Analyzes presence and sensor data to suggest and create automations in Home Assistant.

Future agents can be added following a consistent naming convention and modular structure.

## Project Structure

dynamic_ha_presence/
├── .env # Environment variables (tokens, IPs, etc.)
├── .gitignore # Files and directories to ignore
├── docker-compose.yml # Docker Compose orchestration
├── README.md # This file
├── TODO.md # Project timeline and tasks
├── ble_presence_agent/ # BLE presence detection agent
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── scanner.py
│   ├── mapping.py
│   └── README.md # Agent-specific documentation
├── behavior_agent/ # Behavior analysis and automation agent
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── model.py
│   ├── automation.py
│   └── README.md # Agent-specific documentation
└── common/ # Shared code and configuration
    ├── config.py
    ├── ha_api.py
    ├── db.py
    └── utils.py

## Setup & Usage

1. **Configuration:**
   - Copy `.env.example` (if provided) to `.env` and fill in your Home Assistant details, tokens, and database credentials.
2. **Build & Run:**
   - Build the containers:
     ```bash
     docker-compose build
     ```
   - Run the containers:
     ```bash
     docker-compose up
     ```
3. **Testing & Development:**
   - Refer to the tests/ folder and the TODO.md for further instructions.

## Merging with ai-agent-ble-presence

This project consolidates the BLE presence detection logic from [ai-agent-ble-presence](https://github.com/DeliciousHouse/ai-agent-ble-presence) into a modular structure. Legacy files (e.g. multiple main scripts, redundant test files, agent PDFs) have been refactored or removed for clarity.

## Contributing

Feel free to fork this repository, submit pull requests, and open issues. Please follow the existing code style and update the TODO.md with any new tasks or decisions.

## License

[MIT License](LICENSE)
