import joblib
from sklearn.ensemble import RandomForestClassifier
from evaluate.evaluate import evaluate_model, confusion_matrix


class RFCModel:
    def __init__(self, n_estimators=100, verbose=1, n_jobs=-1, random_state=42):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators, 
            verbose=verbose, 
            n_jobs=n_jobs, 
            random_state=random_state)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        self.y_pred = self.model.predict(X_test)
        return self.y_pred
    
    def evaluate(self, y_test):
        metrics = evaluate_model(y_test, self.y_pred)
        cm = confusion_matrix(y_test, self.y_pred)
        return metrics, cm
    
    def get_feature_importance(self, features):
        feature_importance = dict(zip(features, self.model.feature_importances_))
        feature_importance = dict(sorted(feature_importance.items(), key=lambda item: item[1], reverse=True))
        return feature_importance

    def get_model(self):
        return self.model
    
    def save_model(self, path):
        joblib.dump(self.model, path)

    def load_model(self, path):
        self.model = joblib.load(path)

    def replace_model(self, model):
        self.model = model