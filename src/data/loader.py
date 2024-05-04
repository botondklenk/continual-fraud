import pandas as pd



class DataLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        df = pd.read_csv(self.path)
        X = df.drop('is_fraud', axis=1)
        y = df['is_fraud']
        return X, y
    
    def load_state_by_name(self, state):
        df = pd.read_csv(self.path)
        df_state = df[df['state'] == state]
        X = df_state.drop('is_fraud', axis=1)
        y = df_state['is_fraud']
        return X, y
    
    ## Get state by id, sorted by the number of transactions
    def load_state_by_id(self, state_id):
        df = pd.read_csv(self.path)
        state_counts = df['state'].value_counts().sort_values(ascending=False)
        state_index = state_counts.index.to_list()
        state = state_index[state_id]
        df_state = df[df['state'] == state]
        X = df_state.drop('is_fraud', axis=1)
        y = df_state['is_fraud']
        return X, y
    
    def get_state_list_size(self):
        df = pd.read_csv(self.path)
        state_counts = df['state'].value_counts().sort_values(ascending=False)
        return state_counts.size