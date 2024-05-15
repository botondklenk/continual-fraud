import pandas as pd
import json

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
    def __init__(self, mapping_path='../mappings', mapping_columns=['merchant','city','state','job']):
        self.mapping_path = mapping_path
        self.mapping_columns = mapping_columns
        
    def fit(self, X=None, y=None):
        self.load_mappings()
        return self
    
    def load_mappings(self): 
        mappings = {}
        for column in self.mapping_columns:
            with open(f'{self.mapping_path}/mapping_{column}.json', 'r') as f:
                mappings[column] = json.load(f)
        self.mappings = mappings
    
    def transform(self, X):
        self.df = X.copy()
        self.time_features()
        self.create_dummies()
        self.encode_with_mapping()           
        self.drop_columns()
        return self.df
    
    def drop_columns(self):
        self.df.drop(columns=cols_to_drop,inplace=True)
        
    def create_dummies(self):
        for col in high_risk_categories:
            self.df[col] = self.df['category'].apply(lambda x: 1 if x == col else 0)
        
        self.df['high_risk_job'] = self.df['job'].apply(lambda x: 1 if x in high_risk_jobs else 0)
        
    def encode_with_mapping(self):
        for column in self.mapping_columns:
            if column in self.df.columns:
                self.df[column] = self.df[column].map(self.mappings[column])

    def time_features(self):
        self.df['date'] = pd.to_datetime(self.df['trans_date_trans_time'])
        self.df['month'] = self.df['date'].dt.month
        self.df['day_of_week'] = self.df['date'].dt.dayofweek
        self.df['hour'] = self.df['date'].dt.hour
        # self.df['minute'] = self.df['date'].dt.minute
        # self.df['second'] = self.df['date'].dt.second
        
        # self.df['unix_time'] = self.df['unix_time'] - self.df['unix_time'].min()
        
        self.df['dob'] = pd.to_datetime(self.df['dob'])
        self.df['age'] = ((self.df['date'] - self.df['dob']).dt.days / 365.25).astype(int)
        
        self.df.drop(columns=['trans_date_trans_time','date','dob','unix_time'], axis=1, inplace=True)
        
    def get_feature_names(self):
        return self.df.columns
    
class ContinousDataPreparation(DataPreparation):
    def __init__(self, mapping_path='../mappings'):
        super().__init__(mapping_path, ['merchant','city','state','job', 'category'])
        
    def transform(self, X):
        self.df = X.copy()
        self.time_features()
        self.encode_with_mapping()           
        self.drop_columns()
        return self.df

    # override
    def time_features(self):
        self.df['date'] = pd.to_datetime
        self.df['date'] = pd.to_datetime(self.df['trans_date_trans_time'])
        self.df['month'] = self.df['date'].dt.month
        self.df['day_of_week'] = self.df['date'].dt.dayofweek
        self.df['hour'] = self.df['date'].dt.hour
        self.df['dob'] = pd.to_datetime(self.df['dob'])
        self.df['age'] = ((self.df['date'] - self.df['dob']).dt.days / 365.25).astype(int)
        self.df.drop(columns=['trans_date_trans_time','date','dob'], axis=1, inplace=True)