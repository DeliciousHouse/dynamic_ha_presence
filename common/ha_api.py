import os
import requests

def post_event(occupant, rssi):
    url = f"{os.getenv('HOME_ASSISTANT_API_URL')}/api/events/ble_presence"
    headers = {
        "Authorization": f"Bearer {os.getenv('HA_LONG_LIVED_ACCESS_TOKEN')}",
        "Content-Type": "application/json"
    }
    data = {"occupant": occupant, "rssi": rssi}
    try:
        requests.post(url, json=data, headers=headers)
    except Exception as e:
        print(f"Error posting event: {e}")

def create_automation(automation):
    url = f"{os.getenv('HOME_ASSISTANT_API_URL')}/api/config/automation/config"
    headers = {
        "Authorization": f"Bearer {os.getenv('HA_LONG_LIVED_ACCESS_TOKEN')}",
        "Content-Type": "application/json"
    }
    try:
        requests.post(url, json=automation, headers=headers)
    except Exception as e:
        print(f"Error creating automation: {e}")
