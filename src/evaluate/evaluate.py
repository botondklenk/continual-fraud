import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(y_true, y_pred):
    """
    Evaluate the performance of a classification model.
    
    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.
    
    Returns:
        dict: Dictionary containing evaluation metrics.
    """
    evaluation = {}
    
    # Calculate evaluation metrics
    evaluation['accuracy'] = accuracy_score(y_true, y_pred)
    evaluation['precision'] = precision_score(y_true, y_pred)
    evaluation['recall'] = recall_score(y_true, y_pred)
    evaluation['f1_score'] = f1_score(y_true, y_pred)
    
    return evaluation

def confusion_matrix(y_true, y_pred):
    """
    Compute the confusion matrix.
    
    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.
    
    Returns:
        array: Confusion matrix.
    """
    return confusion_matrix(y_true, y_pred)