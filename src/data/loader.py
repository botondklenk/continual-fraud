import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        df = pd.read_csv(self.path)
        X = df.drop('is_fraud', axis=1)
        y = df['is_fraud']
        return X, y