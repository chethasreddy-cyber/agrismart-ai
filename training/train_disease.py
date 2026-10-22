import os
import cv2
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

CLASSES = ['Healthy', 'Early_Blight', 'Late_Blight', 'Leaf_Mold', 'Potato_Early_Blight', 'Potato_Late_Blight']
IMG_SIZE = (64, 64)

def extract_features(img):
    """Extract color histogram & color moment features from image."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Calculate color histogram for H, S, V channels
    hist_h = cv2.calcHist([hsv], [0], None, [16], [0, 180])
    hist_s = cv2.calcHist([hsv], [1], None, [16], [0, 256])
    hist_v = cv2.calcHist([hsv], [2], None, [16], [0, 256])
    
    hist_features = np.concatenate([hist_h, hist_s, hist_v]).flatten()
    cv2.normalize(hist_features, hist_features)
    
    # Resized raw pixel feature vector
    raw_pixels = cv2.resize(img, (32, 32)).flatten() / 255.0
    
    return np.concatenate([hist_features, raw_pixels])

def load_disease_dataset(data_dir):
    features = []
    labels = []
    
    for idx, label_name in enumerate(CLASSES):
        folder_path = os.path.join(data_dir, label_name)
        if not os.path.exists(folder_path):
            continue
            
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(folder_path, file)
                img = cv2.imread(img_path)
                if img is not None:
                    feat = extract_features(img)
                    features.append(feat)
                    labels.append(idx)
                    
    return np.array(features), np.array(labels)

def train_disease_model():
    print("=" * 50)
    print("TRAINING CROP DISEASE DETECTION MODEL")
    print("=" * 50)
    
    data_dir = os.path.join("dataset", "disease")
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)
    
    X, y = load_disease_dataset(data_dir)
    print(f"[1] Loaded {len(X)} image samples across {len(CLASSES)} classes.")
    
    if len(X) == 0:
        print("[ERROR] No leaf images found. Please run generate_sample_data.py first.")
        return

    # Train / Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Train Random Forest Classifier on visual features
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    print("[2] Image Classifier model training complete.")
    
    # Evaluate Accuracy
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    
    print("\n--- MODEL EVALUATION METRICS ---")
    print(f" -> Classification Accuracy: {accuracy:.2f}%")
    print("--------------------------------\n")
    
    # Save model and class mapping
    model_path = os.path.join(models_dir, "disease_model.pkl")
    classes_path = os.path.join(models_dir, "disease_classes.pkl")
    
    joblib.dump(clf, model_path)
    joblib.dump(CLASSES, classes_path)
    
    print(f"[3] Saved trained classifier model to: {model_path}")
    print(f"[3] Saved class labels map to:         {classes_path}")
    
    # Test Prediction Demo
    test_sample = X_test[0:1]
    probs = clf.predict_proba(test_sample)[0]
    pred_idx = np.argmax(probs)
    confidence = float(probs[pred_idx]) * 100
    
    print("\n--- TEST PREDICTION DEMO ---")
    print(f"Predicted Class : {CLASSES[pred_idx]}")
    print(f"Confidence Score: {confidence:.2f}%")
    print("=" * 50)

if __name__ == "__main__":
    train_disease_model()
