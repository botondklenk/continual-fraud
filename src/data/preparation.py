import pandas as pd
from sklearn.preprocessing import LabelEncoder

high_risk_jobs = [
    'Dancer',
    'Air traffic controller',
    'Careers adviser',
    'Sales promotion account executive',
    'Legal secretary',
    'Personnel officer',
    'Engineer, site',
    'Solicitor',
    'Homeopath',
    'Accountant, chartered',
    'Industrial buyer',
    'Broadcast journalist',
    'Forest/woodland manager',
    'Armed forces technical officer',
    'Information officer',
    'Veterinary surgeon',
    'Ship broker',
    'Contracting civil engineer',
    'Warehouse manager'
]

high_risk_categories = ['misc_net','grocery_pos','shopping_net','shopping_pos','gas_transport']

cols_to_drop = [
    'Unnamed: 0',
    'cc_num',
    'first', 
    'last', 
    'street', 
    'zip', 
    'trans_num', 
    'category', 
    'gender',
    'lat',
    'long',
    'merch_lat',
    'merch_long',
]

class DataPreparation:
    def fit(self, X, y=None):
        self.LE_columns = ['merchant','city','state','job']
        self.LE = {col: LabelEncoder().fit(pd.concat([X[col].astype(str), pd.Series(['Unknown'])])) for col in self.LE_columns}
        return self
    
    def transform(self, X):
        self.df = X.copy()
        self.time_features()
        
        for col in high_risk_categories:
            self.df[col] = self.df['category'].apply(lambda x: 1 if x == col else 0)
        
        self.df['high_risk_job'] = self.df['job'].apply(lambda x: 1 if x in high_risk_jobs else 0)
            
        for col in self.LE_columns:
            try:
                self.df[col] = self.LE[col].transform(self.df[col])
            except ValueError:
                self.df[col] = self.LE[col].transform(self.df[col].map(lambda s: 'Unknown' if s not in self.LE[col].classes_ else s))
                
        self.drop_columns()
        return self.df
    
    def drop_columns(self):
        self.df.drop(columns=cols_to_drop,inplace=True)

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
        
    def get_feature_names(self):
        return self.df.columns