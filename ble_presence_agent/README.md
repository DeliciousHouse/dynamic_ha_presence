# BLE Presence Agent

This agent detects BLE devices and maps their signal strength to occupant presence.

## Files

- **Dockerfile:** Container build instructions.
- **requirements.txt:** Python dependencies.
- **main.py:** Main script that runs BLE scanning and event posting.
- **scanner.py:** Contains BLE scanning logic (using libraries such as Bleak).
- **mapping.py:** Maps BLE device MAC addresses to occupant IDs.

## Setup

1. Ensure your BLE adapter is accessible.
2. Configure the `.env` file at the project root with your Home Assistant URL and token.
3. Build and run using Docker Compose:
   ```bash
   docker-compose build ble_presence_agent
   docker-compose up ble_presence_agent
