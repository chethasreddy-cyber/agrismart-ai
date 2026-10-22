import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_yield_model():
    dataset_path = os.path.join("dataset", "yield_data.csv")
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)
    
    if not os.path.exists(dataset_path):
        print(f"[ERROR] Dataset file not found at {dataset_path}")
        return

    print("=" * 50)
    print("TRAINING CROP YIELD PREDICTION MODEL")
    print("=" * 50)
    
    # 1. Load dataset
    df = pd.read_csv(dataset_path)
    print(f"[1] Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    
    # 2. Define Features and Target
    # Target column is Yield_Tons_Per_Acre
    X = df.drop(columns=['Yield_Tons_Per_Acre'])
    y = df['Yield_Tons_Per_Acre']
    
    categorical_cols = ['Crop', 'Season']
    numerical_cols = [col for col in X.columns if col not in categorical_cols]
    
    print(f"    - Categorical Features: {categorical_cols}")
    print(f"    - Numerical Features:   {numerical_cols}")
    
    # 3. Create Preprocessor (One-Hot Encoding for Categoricals)
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_cols),
            ('num', 'passthrough', numerical_cols)
        ]
    )
    
    # 4. Fit & transform features
    X_processed = preprocessor.fit_transform(X)
    
    # 5. Train/Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=0.2, random_state=42
    )
    
    # 6. Train Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("[2] Random Forest Regressor training complete.")
    
    # 7. Evaluate Model
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print("\n--- MODEL EVALUATION METRICS ---")
    print(f" -> Mean Absolute Error (MAE) : {mae:.4f} tons/acre")
    print(f" -> Root Mean Sq. Error (RMSE): {rmse:.4f} tons/acre")
    print(f" -> R-squared Score (R²)      : {r2:.4f} ({r2 * 100:.2f}%)")
    print("--------------------------------\n")
    
    # 8. Save Trained Model and Preprocessor
    model_path = os.path.join(models_dir, "yield_model.pkl")
    preprocessor_path = os.path.join(models_dir, "yield_preprocessor.pkl")
    
    joblib.dump(model, model_path)
    joblib.dump(preprocessor, preprocessor_path)
    print(f"[3] Saved trained model to: {model_path}")
    print(f"[3] Saved preprocessor to:  {preprocessor_path}")
    
    # 9. Quick Prediction Test Demo
    sample_input = pd.DataFrame([{
        'Crop': 'Tomato',
        'Season': 'Rabi',
        'Area_Acres': 2.5,
        'Soil_pH': 6.5,
        'Nitrogen_N': 90,
        'Phosphorus_P': 45,
        'Potassium_K': 60,
        'Temperature_C': 26.5,
        'Humidity_pct': 65.0,
        'Rainfall_mm': 750.0
    }])
    
    sample_processed = preprocessor.transform(sample_input)
    predicted_yield = model.predict(sample_processed)[0]
    
    print("\n--- TEST PREDICTION DEMO ---")
    print(f"Input: Tomato, 2.5 Acres, pH 6.5, NPK (90,45,60), 26.5C, 65% Hum, 750mm Rain")
    print(f"Predicted Yield: {predicted_yield:.2f} tons/acre")
    print("=" * 50)

if __name__ == "__main__":
    train_yield_model()
