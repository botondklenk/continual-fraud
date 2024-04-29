from sklearn.preprocessing import StandardScaler

def feature_scaling(df, columns):
    """
    Apply feature scaling to the specified columns of a DataFrame.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to be scaled.
    - columns (list): A list of column names to be scaled.

    Returns:
    - df (pandas.DataFrame): The DataFrame with the scaled columns.
    """
    features = df[columns]
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)
    df[columns] = features
    
    return df