import time
import pandas as pd
from model import BehaviorModel
from automation import propose_automation
from common.db import fetch_presence_data
from common.config import load_env

def main():
    load_env()
    model = BehaviorModel()
    while True:
        data = fetch_presence_data()
        df = pd.DataFrame(data)
        patterns = model.analyze(df)
        for pattern in patterns:
            propose_automation(pattern)
        time.sleep(3600)

if __name__ == "__main__":
    main()
