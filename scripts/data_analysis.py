# scripts/data_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('data/equipment_data.csv')

# Display first few rows
print("First five rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical summary:")
print(df.describe())

# Set the theme for plots (dark background)
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#1e1e1e", "figure.facecolor": "#121212"})

# Correlation matrix
corr_matrix = df.corr()

# Save figures to '/app/data' directory
output_dir = 'data'

plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5,
    linecolor='gray',
    annot_kws={"color": "white"},
    cbar_kws={'format': '%.2f'},
    fmt=".2f"
)
plt.title('Correlation Matrix', color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(rotation=0, color='white')
plt.tight_layout()
plt.savefig(f'{output_dir}/correlation_matrix.png', dpi=300, transparent=True)
plt.close()

# Distribution plots
for column in df.columns:
    plt.figure()
    sns.histplot(df[column], kde=True, color='skyblue')
    plt.title(f'Distribution of {column}', color='white')
    plt.xlabel(column, color='white')
    plt.ylabel('Frequency', color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{column}_distribution.png', dpi=300, transparent=True)
    plt.close()
