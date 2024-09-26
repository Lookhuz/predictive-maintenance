# model/preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

def preprocess_data(X: pd.DataFrame) -> tuple:
    """Scale features and save the scaler."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Save the scaler
    with open('model/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    return X_scaled, scaler
