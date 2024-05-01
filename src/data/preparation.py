import pandas as pd
from sklearn.preprocessing import LabelEncoder
from features.feature_scaler import feature_scaling

class DataPreparation:
    def __init__(self, path, time_feature='drop'):
        self.time_feature = time_feature
        self.df = self.load_data(path)
        self.df = self.data_preprocessing()
        #self.df = self.feature_scaling()

    def load_data(self, path):
        data = pd.read_csv(path)
        return data

    # TODO: drop fraud column
    def data_preprocessing(self):
        self.drop_columns()
        #self.label_encoding()
        self.time_features()
        self.df.fillna(0, inplace=True)
        return self.df;

    def label_encoding(self):
        label_encoder = LabelEncoder()
        for column in self.df.columns:
            if self.df[column].dtype == 'object':
                self.df[column] = label_encoder.fit_transform(self.df[column])

    def time_features(self):
        if self.time_feature == 'drop':
            self.df.drop('trans_date_trans_time', axis=1, inplace=True)

    def drop_columns(self):
        self.df.drop(columns=['Unnamed: 0','cc_num','first', 'last', 'street', 'zip', 'trans_num'],inplace=True)

    def info(self):
        print(self.df.info())
        print(self.df.shape)
    
    def get_data(self):
        return self.df

    def feature_scaling(self):
        self.df = feature_scaling(self.df, ['amt'])
        return self.df