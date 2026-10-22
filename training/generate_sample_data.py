import os
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw

def create_sample_yield_dataset():
    """Generates a realistic synthetic Crop Yield Dataset for training."""
    os.makedirs("dataset", exist_ok=True)
    filepath = os.path.join("dataset", "yield_data.csv")
    
    np.random.seed(42)
    n_samples = 500
    
    crops = ['Tomato', 'Potato', 'Rice', 'Wheat', 'Maize']
    seasons = ['Kharif', 'Rabi', 'Whole Year']
    
    data = []
    for _ in range(n_samples):
        crop = np.random.choice(crops)
        season = np.random.choice(seasons)
        area = round(float(np.random.uniform(1.0, 10.0)), 2)
        soil_ph = round(float(np.random.uniform(5.5, 7.5)), 2)
        nitrogen = int(np.random.randint(20, 140))
        phosphorus = int(np.random.randint(10, 80))
        potassium = int(np.random.randint(15, 100))
        temperature = round(float(np.random.uniform(18.0, 35.0)), 1)
        humidity = round(float(np.random.uniform(40.0, 85.0)), 1)
        rainfall = round(float(np.random.uniform(300.0, 1200.0)), 1)
        
        # Formula for realistic crop yield (tons per acre)
        base_yield = {
            'Tomato': 4.5,
            'Potato': 5.0,
            'Rice': 3.5,
            'Wheat': 3.0,
            'Maize': 2.8
        }[crop]
        
        # Add environmental variations
        ph_factor = 1.0 - abs(soil_ph - 6.5) * 0.1
        npk_factor = (nitrogen * 0.4 + phosphorus * 0.3 + potassium * 0.3) / 100.0
        weather_factor = (temperature / 30.0) * (humidity / 70.0)
        
        yield_val = base_yield * ph_factor * npk_factor * weather_factor + np.random.normal(0, 0.3)
        yield_val = round(max(0.5, float(yield_val)), 2)
        
        data.append({
            'Crop': crop,
            'Season': season,
            'Area_Acres': area,
            'Soil_pH': soil_ph,
            'Nitrogen_N': nitrogen,
            'Phosphorus_P': phosphorus,
            'Potassium_K': potassium,
            'Temperature_C': temperature,
            'Humidity_pct': humidity,
            'Rainfall_mm': rainfall,
            'Yield_Tons_Per_Acre': yield_val
        })
        
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"[OK] Generated {filepath} with {len(df)} rows.")

def create_sample_disease_images():
    """Generates synthetic leaf images for multi-crop disease classes."""
    categories = ['Healthy', 'Early_Blight', 'Late_Blight', 'Leaf_Mold', 'Potato_Early_Blight', 'Potato_Late_Blight']
    base_dir = os.path.join("dataset", "disease")
    
    for cat in categories:
        cat_dir = os.path.join(base_dir, cat)
        os.makedirs(cat_dir, exist_ok=True)
        
        for i in range(15):
            img_path = os.path.join(cat_dir, f"{cat.lower()}_{i+1}.jpg")
            if not os.path.exists(img_path):
                img = Image.new('RGB', (128, 128), color=(34, 139, 34))
                draw = ImageDraw.Draw(img)
                draw.ellipse([20, 10, 108, 118], fill=(46, 139, 87))
                
                if 'Early_Blight' in cat:
                    draw.ellipse([40, 40, 65, 65], fill=(139, 69, 19))
                    draw.ellipse([70, 70, 90, 90], fill=(139, 69, 19))
                elif 'Late_Blight' in cat:
                    draw.polygon([(30, 30), (70, 20), (60, 80), (20, 60)], fill=(47, 79, 79))
                elif cat == 'Leaf_Mold':
                    draw.ellipse([30, 50, 75, 95], fill=(218, 165, 32))
                
                img.save(img_path)
    print(f"[OK] Created multi-crop sample leaf image dataset under {base_dir}")

if __name__ == "__main__":
    create_sample_yield_dataset()
    create_sample_disease_images()
