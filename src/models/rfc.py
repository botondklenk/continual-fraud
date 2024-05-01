import joblib
from sklearn.ensemble import RandomForestClassifier
from evaluate.evaluate import evaluate_model, confusion_matrix


class RFCModel:
    def __init__(self, n_estimators=10, max_depth=4, random_state=42):
        self.model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)
    
    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        evaluation = evaluate_model(y_test, y_pred)
        self.y_test = y_test
        self.y_pred = y_pred
        metrics = [(evaluation['recall'], evaluation['precision'], evaluation['f1_score'], evaluation['accuracy'])]
        return metrics
    
    def confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_pred)
    
    def get_feature_importance(self, X_train):
        features = X_train.columns
        importance = self.model.feature_importances_
        feature_importance = dict(sorted(zip(features, importance).items(), key=lambda item: item[1], reverse=True))
        return feature_importance

    def get_model(self):
        return self.model
    
    def save_model(self, path):
        joblib.dump(self.model, path)

    def load_model(self, path):
        self.model = joblib.load(path)

    def replace_model(self, model):
        self.model = model