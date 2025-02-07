
import pandas as pd
from sklearn.cluster import KMeans

class BehaviorModel:
    def __init__(self):
        self.model = KMeans(n_clusters=2)

    def analyze(self, df: pd.DataFrame):
        if df.empty:
            return []
        X = df[['rssi']].values
        self.model.fit(X)
        labels = self.model.labels_
        patterns = [{"cluster": int(label), "mean_rssi": float(x)} for label, x in zip(labels, X.flatten())]
        return patterns
