import os
import pandas as pd

def inspect_dataset():
    filepath = os.path.join("dataset", "yield_data.csv")
    
    if not os.path.exists(filepath):
        print(f"[ERROR] {filepath} not found. Please run generate_sample_data.py first!")
        return

    print("=" * 50)
    print("CROP YIELD DATASET INSPECTION")
    print("=" * 50)
    
    df = pd.read_csv(filepath)
    
    print(f"\nTotal Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")
    
    print("\nColumn Names and Data Types:")
    print("-" * 50)
    for col in df.columns:
        print(f" * {col:<20} | Type: {str(df[col].dtype):<10} | Missing Values: {df[col].isnull().sum()}")
        
    print("\nFirst 5 Rows Preview:")
    print("-" * 50)
    print(df.head())
    
    print("\nNumerical Summary:")
    print("-" * 50)
    print(df.describe().T[['mean', 'std', 'min', '50%', 'max']])
    print("=" * 50)

if __name__ == "__main__":
    inspect_dataset()
