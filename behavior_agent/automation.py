from common.ha_api import create_automation

def propose_automation(pattern, area, entity_id):
    automation = {
        "alias": f"Auto Automation for cluster {pattern['cluster']} in {area}",
        "trigger": {
            "platform": "time",
            "at": "18:00:00"
        },
        "action": {
            "service": "light.toggle",
            "entity_id": entity_id
        }
    }
    create_automation(automation)
