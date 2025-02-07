import time
import pandas as pd
from model import BehaviorModel
from automation import propose_automation
from common.db import fetch_presence_data
from common.config import load_env
from apscheduler.schedulers.background import BackgroundScheduler

def fetch_and_process_data(model):
    data = fetch_presence_data()
    df = pd.DataFrame(data)
    patterns = model.analyze(df)
    for pattern in patterns:
        propose_automation(pattern)

def main():
    print("Behavior agent started.")
    load_env()
    model = BehaviorModel()
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: fetch_and_process_data(model), 'interval', hours=1)
    scheduler.start()
    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    main()
