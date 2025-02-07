import requests
from common.config import get_env

def post_event(occupant, rssi):
    url = f"{get_env('HA_BASE_URL')}/api/events/ble_presence"
    headers = {
        "Authorization": f"Bearer {get_env('HA_TOKEN')}",
        "Content-Type": "application/json"
    }
    data = {"occupant": occupant, "rssi": rssi}
    try:
        requests.post(url, json=data, headers=headers)
    except Exception as e:
        print(f"Error posting event: {e}")

def create_automation(automation):
    url = f"{get_env('HA_BASE_URL')}/api/config/automation/config"
    headers = {
        "Authorization": f"Bearer {get_env('HA_TOKEN')}",
        "Content-Type": "application/json"
    }
    try:
        requests.post(url, json=automation, headers=headers)
    except Exception as e:
        print(f"Error creating automation: {e}")
