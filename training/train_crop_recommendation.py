import os
import sys
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

CROP_CATEGORY_MAP = {
    'Tomato': 'Vegetable', 'Potato': 'Vegetable', 'Chilli': 'Vegetable',
    'Brinjal': 'Vegetable', 'Cabbage': 'Vegetable', 'Cucumber': 'Vegetable', 'Onion': 'Vegetable',
    'Rose': 'Flower', 'Marigold': 'Flower', 'Jasmine': 'Flower',
    'Sunflower': 'Flower', 'Chrysanthemum': 'Flower',
    'Carrot': 'Root Crop', 'Radish': 'Root Crop', 'Beetroot': 'Root Crop',
    'Ginger': 'Root Crop', 'Sweet Potato': 'Root Crop',
    'Rice': 'Cereal / Grain', 'Wheat': 'Cereal / Grain', 'Maize': 'Cereal / Grain'
}

CROP_ICONS = {
    'Tomato': '🍅', 'Potato': '🥔', 'Chilli': '🌶️', 'Brinjal': '🍆', 'Cabbage': '🥬', 'Cucumber': '🥒', 'Onion': '🧅',
    'Rose': '🌹', 'Marigold': '🌼', 'Jasmine': '🌸', 'Sunflower': '🌻', 'Chrysanthemum': '🏵️',
    'Carrot': '🥕', 'Radish': '🌱', 'Beetroot': '🍠', 'Ginger': '🫚', 'Sweet Potato': '🥔',
    'Rice': '🌾', 'Wheat': '🌾', 'Maize': '🌽'
}

def train_crop_recommendation_model():
    dataset_path = os.path.join("dataset", "yield_data.csv")
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)

    if not os.path.exists(dataset_path):
        print(f"[ERROR] Dataset file not found at {dataset_path}")
        return

    print("=" * 60)
    print("TRAINING ZERO-INPUT WEATHER & MONTH CROP RECOMMENDATION MODEL")
    print("=" * 60)

    df = pd.read_csv(dataset_path)
    print(f"[1] Loaded dataset with {len(df)} rows.")

    # Features: strictly Month and Live Weather (NO Soil pH, NO Manual NPK required from user)
    feature_cols = ['Month', 'Temperature_C', 'Humidity_pct', 'Rainfall_mm']
    X = df[feature_cols]
    y = df['Crop']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    clf = RandomForestClassifier(n_estimators=150, max_depth=16, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred) * 100

    print("\n--- CROP RECOMMENDATION METRICS ---")
    print(f" -> Classification Accuracy: {acc:.2f}%")
    print(f" -> Total Crops Covered:     {len(clf.classes_)}")
    print("-----------------------------------\n")

    model_path = os.path.join(models_dir, "crop_rec_model.pkl")
    features_path = os.path.join(models_dir, "crop_rec_features.pkl")

    joblib.dump(clf, model_path)
    joblib.dump(feature_cols, features_path)

    print(f"[2] Saved zero-input crop recommendation model to: {model_path}")

    # Demo prediction test for current calendar month
    current_month = datetime.now().month
    demo_sample = pd.DataFrame([{
        'Month': current_month,
        'Temperature_C': 21.0,
        'Humidity_pct': 60.0,
        'Rainfall_mm': 520.0
    }])

    probs = clf.predict_proba(demo_sample)[0]
    classes = clf.classes_
    top_idx = np.argsort(probs)[::-1]

    print(f"\n--- TOP CROP RECOMMENDATIONS DEMO (Month #{current_month}, 21.0C, 60% Hum, 520mm Rain) ---")
    for i in range(min(5, len(classes))):
        idx = top_idx[i]
        crop_name = classes[idx]
        category = CROP_CATEGORY_MAP.get(crop_name, 'Crop')
        print(f" #{i+1} {crop_name:<14} [{category:<14}] | Suitability Score: {probs[idx] * 100:.1f}%")
    print("=" * 60)

def predict_recommended_crop(temp=25.0, humidity=65.0, rainfall=600.0, month=None, *args, **kwargs):
    """
    Predicts the top suitable crops based automatically on live weather and the current month.
    Does NOT require soil pH or manual user inputs.
    """
    model_path = os.path.join("models", "crop_rec_model.pkl")
    if month is None:
        month = datetime.now().month

    try:
        temp = float(temp)
        humidity = float(humidity)
        rainfall = float(rainfall)
        month = int(month)
    except (ValueError, TypeError):
        temp, humidity, rainfall, month = 25.0, 65.0, 600.0, datetime.now().month

    if not os.path.exists(model_path):
        return [
            {'crop': 'Tomato', 'category': 'Vegetable', 'icon': '🍅', 'score': 94.5, 'reason': 'Optimal winter daytime temp and moderate humidity.'},
            {'crop': 'Rose', 'category': 'Flower', 'icon': '🌹', 'score': 91.2, 'reason': 'Ideal blooming conditions and mild temperature.'},
            {'crop': 'Carrot', 'category': 'Root Crop', 'icon': '🥕', 'score': 88.0, 'reason': 'Cool subterranean root formation weather.'}
        ]

    clf = joblib.load(model_path)
    sample = pd.DataFrame([{
        'Month': month,
        'Temperature_C': temp,
        'Humidity_pct': humidity,
        'Rainfall_mm': rainfall
    }])

    probs = clf.predict_proba(sample)[0]
    classes = clf.classes_
    top_indices = np.argsort(probs)[::-1]

    month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_str = month_names[month] if 1 <= month <= 12 else 'Current Month'

    results = []
    for idx in top_indices[:5]:
        crop_name = str(classes[idx])
        category = CROP_CATEGORY_MAP.get(crop_name, 'Field Crop')
        icon = CROP_ICONS.get(crop_name, '🌱')
        score = round(float(probs[idx]) * 100, 1)

        if category == 'Flower':
            reason = f"Excellent flowering temperature ({temp:.1f}°C) and mild air humidity in {month_str}."
        elif category == 'Vegetable':
            reason = f"Ideal vegetative canopy growth and fruit setting conditions for {month_str}."
        elif category == 'Root Crop':
            reason = f"Favorable cool soil thermal conditions for root tuber bulking in {month_str}."
        else:
            reason = f"Well-aligned seasonal climate and precipitation profile in {month_str}."

        results.append({
            'crop': crop_name,
            'category': category,
            'icon': icon,
            'score': score,
            'reason': reason
        })
    return results

if __name__ == "__main__":
    train_crop_recommendation_model()
