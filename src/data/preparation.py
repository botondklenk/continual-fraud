import pandas as pd
from sklearn.preprocessing import LabelEncoder

class DataPreparation:
    def fit(self, X, y=None):
        self.LE_columns = ['merchant','city','state','job']
        self.LE = {col: LabelEncoder().fit(pd.concat([X[col].astype(str), pd.Series(['Unknown'])])) for col in self.LE_columns}
        return self
    
    def transform(self, X):
        self.df = X.copy()
        self.drop_columns()
        self.time_features()
        
        self.dummy_columns = ['category','gender']
        dummies_df = pd.get_dummies(self.df[self.dummy_columns], drop_first=True)
        self.df.drop(self.dummy_columns, axis=1, inplace=True)
        self.df = pd.concat([self.df, dummies_df], axis=1)
            
        for col in self.LE_columns:
            try:
                self.df[col] = self.LE[col].transform(self.df[col])
            except ValueError:
                self.df[col] = self.LE[col].transform(self.df[col].map(lambda s: 'Unknown' if s not in self.LE[col].classes_ else s))
        return self.df
    
    def drop_columns(self):
        self.df.drop(columns=['Unnamed: 0','cc_num','first', 'last', 'street', 'zip', 'trans_num'],inplace=True)

    def time_features(self):
        self.df['date'] = pd.to_datetime(self.df['trans_date_trans_time'])
        self.df['month'] = self.df['date'].dt.month
        self.df['day_of_week'] = self.df['date'].dt.dayofweek
        self.df['hour'] = self.df['date'].dt.hour
        # self.df['minute'] = self.df['date'].dt.minute
        # self.df['second'] = self.df['date'].dt.second
        
        self.df['unix_time'] = self.df['unix_time'] - self.df['unix_time'].min()
        
        self.df['dob'] = pd.to_datetime(self.df['dob'])
        self.df['age'] = ((self.df['date'] - self.df['dob']).dt.days / 365.25).astype(int)
        
        self.df.drop(columns=['trans_date_trans_time','date','dob'], axis=1, inplace=True)