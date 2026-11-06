import cv2
import numpy as np

def calculate_disease_severity(image_path_or_array):
    """
    Calculates disease severity percentage across diverse plant species (flowers, vegetables, roots, grains)
    using multi-band HSV color thresholding & contour extraction.
    Formula: Disease Percentage = (Diseased Area / Total Leaf Area) * 100
    
    Thresholds:
      0% - 20%   -> Low
     21% - 50%   -> Medium
     51% - 100%  -> High
    """
    if isinstance(image_path_or_array, str):
        img = cv2.imread(image_path_or_array)
    else:
        img = image_path_or_array

    if img is None:
        return {
            'is_valid_leaf': False,
            'affected_percentage': 0.0,
            'severity': 'None',
            'total_leaf_pixels': 0,
            'diseased_pixels': 0
        }

    img = cv2.resize(img, (256, 256))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 1. Healthy green leaf tissue range
    lower_green = np.array([25, 35, 35])
    upper_green = np.array([88, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # 2. Diseased Symptom Bands:
    # a) Yellowish / chlorotic / light-brown lesions (Blights, Downy Mildew, Leaf Mold, Wilt)
    mask_yellow_brown = cv2.inRange(hsv, np.array([10, 40, 40]), np.array([24, 255, 255]))

    # b) Dark necrotic brown & black spots (Black Spot, Anthracnose, Late Blight)
    mask_dark_necrotic = cv2.inRange(hsv, np.array([0, 30, 10]), np.array([180, 255, 75]))

    # c) Reddish-orange rust pustules (Leaf Rust)
    mask_rust1 = cv2.inRange(hsv, np.array([0, 70, 70]), np.array([10, 255, 255]))
    mask_rust2 = cv2.inRange(hsv, np.array([170, 70, 70]), np.array([180, 255, 255]))
    mask_rust = cv2.bitwise_or(mask_rust1, mask_rust2)

    # d) White / powdery mildew fungal coating (Powdery Mildew)
    # Low saturation (<45) and high value (>175)
    mask_powdery = cv2.inRange(hsv, np.array([0, 0, 175]), np.array([180, 50, 255]))

    # Combine all diseased symptom masks
    mask_diseased = cv2.bitwise_or(mask_yellow_brown, mask_dark_necrotic)
    mask_diseased = cv2.bitwise_or(mask_diseased, mask_rust)
    mask_diseased = cv2.bitwise_or(mask_diseased, mask_powdery)

    # Total plant leaf surface area (green healthy tissue + infected regions)
    mask_total_leaf = cv2.bitwise_or(mask_green, mask_diseased)

    total_leaf_pixels = cv2.countNonZero(mask_total_leaf)
    diseased_pixels = cv2.countNonZero(mask_diseased)

    # Safety Guard: Ensure image contains actual leaf/plant matter (>4% area, sufficient texture)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    std_dev = float(np.std(gray))

    if total_leaf_pixels < 2500 or std_dev < 1.0:
        return {
            'is_valid_leaf': False,
            'affected_percentage': 0.0,
            'severity': 'None',
            'total_leaf_pixels': int(total_leaf_pixels),
            'diseased_pixels': 0
        }

    # Calculate Affected Percentage
    affected_percentage = (diseased_pixels / float(total_leaf_pixels)) * 100.0
    affected_percentage = round(float(min(100.0, max(0.0, affected_percentage))), 1)

    # Severity Level
    if affected_percentage <= 20.0:
        severity = "Low"
    elif affected_percentage <= 50.0:
        severity = "Medium"
    else:
        severity = "High"

    return {
        'is_valid_leaf': True,
        'affected_percentage': affected_percentage,
        'severity': severity,
        'total_leaf_pixels': int(total_leaf_pixels),
        'diseased_pixels': int(diseased_pixels)
    }

if __name__ == "__main__":
    import os
    sample_path = os.path.join("dataset", "disease", "Early_Blight", "early_blight_1.jpg")
    if os.path.exists(sample_path):
        res = calculate_disease_severity(sample_path)
        print("Leaf Severity Test:", res)
