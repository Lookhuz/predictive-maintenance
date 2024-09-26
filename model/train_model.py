# model/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import pickle
from model.preprocessing import preprocess_data

# Load the data
df = pd.read_csv('data/equipment_data.csv')

# Features and target variable
X = df.drop('failure', axis=1)
y = df['failure']

# Feature scaling and save scaler
X_scaled, scaler = preprocess_data(X)

# Check class distribution
print("Class distribution before resampling:")
print(y.value_counts())

# Apply SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

print("Class distribution after resampling:")
print(y_resampled.value_counts())

# Split the resampled data
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
)

# Initialize the model with hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

# Train the model
grid_search.fit(X_train, y_train)
model = grid_search.best_estimator_

# Evaluate the model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save the model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
