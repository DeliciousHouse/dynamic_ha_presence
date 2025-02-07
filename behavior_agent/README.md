# behavior_agent

The **behavior_agent** analyzes presence and sensor data to determine household behavior patterns. Based on the detected patterns, it can suggest or automatically create automations in Home Assistant.

## Files

- **Dockerfile:** Container build instructions.
- **requirements.txt:** Python dependencies.
- **main.py:** Main script that periodically analyzes data and triggers automation proposals.
- **model.py:** Contains the AI/model logic (e.g., a simple clustering or forecasting model).
- **automation.py:** Handles creation of automation suggestions via the Home Assistant API.

## Setup

1. Configure your Home Assistant API and database settings in the `.env` file.
2. Build and run using Docker Compose:
   ```bash
   docker-compose build behavior_agent
   docker-compose up behavior_agent
