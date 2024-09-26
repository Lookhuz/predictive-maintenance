# data/generate_data.py

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# Generate synthetic data
data = {
    'temperature': np.random.normal(loc=75, scale=10, size=n_samples),
    'vibration': np.random.normal(loc=0.5, scale=0.1, size=n_samples),
    'pressure': np.random.normal(loc=30, scale=5, size=n_samples),
    'operational_hours': np.random.randint(low=100, high=10000, size=n_samples),
}

df = pd.DataFrame(data)

# Feature engineering
df['temp_pressure_interaction'] = df['temperature'] * df['pressure']
df['vibration_squared'] = df['vibration'] ** 2

# Simulate failure occurrence
df['failure'] = np.where(
    (df['temperature'] > 90) | (df['vibration'] > 0.7) | (df['pressure'] > 40), 1, 0
)

# Save to CSV
df.to_csv('data/equipment_data.csv', index=False)
