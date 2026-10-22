import cv2
import numpy as np

def calculate_disease_severity(image_path_or_array):
    """
    Calculates disease severity percentage using HSV color thresholding & contour extraction.
    Formula: Disease Percentage = (Diseased Area / Total Leaf Area) * 100
    
    Thresholds (Project Methodology):
      0% - 20%   -> Low
     21% - 50%   -> Medium
     51% - 100%  -> High
    """
    # 1. Load image
    if isinstance(image_path_or_array, str):
        img = cv2.imread(image_path_or_array)
    else:
        img = image_path_or_array

    if img is None:
        # Fallback default if image fails to load
        return {
            'is_valid_leaf': False,
            'affected_percentage': 0.0,
            'severity': 'None',
            'total_leaf_pixels': 0,
            'diseased_pixels': 0
        }

    # Resize image for standard analysis
    img = cv2.resize(img, (256, 256))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 2. Extract Total Leaf Area (Greenish + Yellowish + Brownish regions)
    # Green leaf range
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Diseased brown / yellow lesion range
    lower_yellow_brown = np.array([10, 40, 40])
    upper_yellow_brown = np.array([24, 255, 255])
    mask_diseased1 = cv2.inRange(hsv, lower_yellow_brown, upper_yellow_brown)

    lower_dark_brown = np.array([0, 50, 20])
    upper_dark_brown = np.array([9, 255, 200])
    mask_diseased2 = cv2.inRange(hsv, lower_dark_brown, upper_dark_brown)

    mask_diseased = cv2.bitwise_or(mask_diseased1, mask_diseased2)
    mask_total_leaf = cv2.bitwise_or(mask_green, mask_diseased)

    total_leaf_pixels = cv2.countNonZero(mask_total_leaf)
    diseased_pixels = cv2.countNonZero(mask_diseased)

    # Validate that image contains a real leaf/plant (minimum 4% of pixels)
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

    # 3. Calculate Disease Percentage
    affected_percentage = (diseased_pixels / float(total_leaf_pixels)) * 100.0
    affected_percentage = round(float(min(100.0, max(0.0, affected_percentage))), 1)

    # 4. Determine Severity Level
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
    sample_img_path = os.path.join("dataset", "disease", "Early_Blight", "early_blight_1.jpg")
    if os.path.exists(sample_img_path):
        res = calculate_disease_severity(sample_img_path)
        print("=" * 50)
        print("DISEASE SEVERITY ASSESSMENT TEST")
        print("=" * 50)
        print(f"Image Analysed     : {sample_img_path}")
        print(f"Total Leaf Area    : {res['total_leaf_pixels']} pixels")
        print(f"Diseased Area      : {res['diseased_pixels']} pixels")
        print(f"Affected Area (%)  : {res['affected_percentage']}%")
        print(f"Severity Category  : {res['severity']}")
        print("=" * 50)
