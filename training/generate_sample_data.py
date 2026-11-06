import os
import sys
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def create_sample_yield_dataset():
    """Generates a realistic synthetic Crop Yield & Recommendation Dataset for 20 multi-category crops."""
    os.makedirs("dataset", exist_ok=True)
    filepath = os.path.join("dataset", "yield_data.csv")
    
    np.random.seed(42)
    n_samples_per_crop = 60  # 60 * 20 = 1200 high-quality samples
    
    # 20 crops across 4 major agricultural categories with distinct agronomic profiles
    crops_info = {
        # Vegetables
        'Tomato': {
            'cat': 'Vegetable', 'base_yield': 4.8, 'season': 'Rabi',
            'temp_mean': 22.0, 'temp_std': 3.0,
            'hum_mean': 62.0, 'hum_std': 6.0,
            'rain_mean': 550.0, 'rain_std': 60.0,
            'opt_months': [10, 11, 12, 1, 2]
        },
        'Potato': {
            'cat': 'Vegetable', 'base_yield': 5.2, 'season': 'Rabi',
            'temp_mean': 18.0, 'temp_std': 2.5,
            'hum_mean': 68.0, 'hum_std': 5.0,
            'rain_mean': 480.0, 'rain_std': 50.0,
            'opt_months': [10, 11, 12, 1]
        },
        'Chilli': {
            'cat': 'Vegetable', 'base_yield': 2.8, 'season': 'Kharif',
            'temp_mean': 28.0, 'temp_std': 3.0,
            'hum_mean': 72.0, 'hum_std': 6.0,
            'rain_mean': 820.0, 'rain_std': 80.0,
            'opt_months': [6, 7, 8, 9]
        },
        'Brinjal': {
            'cat': 'Vegetable', 'base_yield': 4.5, 'season': 'Whole Year',
            'temp_mean': 25.5, 'temp_std': 3.5,
            'hum_mean': 66.0, 'hum_std': 7.0,
            'rain_mean': 680.0, 'rain_std': 70.0,
            'opt_months': [1, 2, 6, 7, 10]
        },
        'Cabbage': {
            'cat': 'Vegetable', 'base_yield': 6.0, 'season': 'Rabi',
            'temp_mean': 16.5, 'temp_std': 2.0,
            'hum_mean': 75.0, 'hum_std': 5.0,
            'rain_mean': 500.0, 'rain_std': 50.0,
            'opt_months': [11, 12, 1, 2]
        },
        'Cucumber': {
            'cat': 'Vegetable', 'base_yield': 3.8, 'season': 'Zaid',
            'temp_mean': 31.0, 'temp_std': 3.0,
            'hum_mean': 52.0, 'hum_std': 6.0,
            'rain_mean': 380.0, 'rain_std': 40.0,
            'opt_months': [3, 4, 5]
        },
        'Onion': {
            'cat': 'Vegetable', 'base_yield': 5.5, 'season': 'Rabi',
            'temp_mean': 20.0, 'temp_std': 2.5,
            'hum_mean': 58.0, 'hum_std': 5.0,
            'rain_mean': 450.0, 'rain_std': 50.0,
            'opt_months': [10, 11, 12, 1]
        },

        # Flowers
        'Rose': {
            'cat': 'Flower', 'base_yield': 1.8, 'season': 'Whole Year',
            'temp_mean': 21.0, 'temp_std': 2.5,
            'hum_mean': 60.0, 'hum_std': 5.0,
            'rain_mean': 520.0, 'rain_std': 50.0,
            'opt_months': [10, 11, 12, 1, 2]
        },
        'Marigold': {
            'cat': 'Flower', 'base_yield': 3.2, 'season': 'Whole Year',
            'temp_mean': 24.0, 'temp_std': 3.0,
            'hum_mean': 64.0, 'hum_std': 6.0,
            'rain_mean': 580.0, 'rain_std': 60.0,
            'opt_months': [7, 8, 9, 10, 11]
        },
        'Jasmine': {
            'cat': 'Flower', 'base_yield': 1.5, 'season': 'Whole Year',
            'temp_mean': 29.5, 'temp_std': 2.5,
            'hum_mean': 74.0, 'hum_std': 5.0,
            'rain_mean': 860.0, 'rain_std': 80.0,
            'opt_months': [3, 4, 5, 6, 7]
        },
        'Sunflower': {
            'cat': 'Flower', 'base_yield': 2.2, 'season': 'Kharif',
            'temp_mean': 27.0, 'temp_std': 2.5,
            'hum_mean': 55.0, 'hum_std': 6.0,
            'rain_mean': 620.0, 'rain_std': 60.0,
            'opt_months': [6, 7, 8]
        },
        'Chrysanthemum': {
            'cat': 'Flower', 'base_yield': 2.6, 'season': 'Rabi',
            'temp_mean': 19.0, 'temp_std': 2.0,
            'hum_mean': 65.0, 'hum_std': 5.0,
            'rain_mean': 420.0, 'rain_std': 40.0,
            'opt_months': [9, 10, 11, 12]
        },

        # Root & Tuber Crops
        'Carrot': {
            'cat': 'Root Crop', 'base_yield': 5.8, 'season': 'Rabi',
            'temp_mean': 15.5, 'temp_std': 2.0,
            'hum_mean': 70.0, 'hum_std': 5.0,
            'rain_mean': 460.0, 'rain_std': 45.0,
            'opt_months': [10, 11, 12, 1]
        },
        'Radish': {
            'cat': 'Root Crop', 'base_yield': 6.2, 'season': 'Rabi',
            'temp_mean': 17.0, 'temp_std': 2.0,
            'hum_mean': 65.0, 'hum_std': 5.0,
            'rain_mean': 410.0, 'rain_std': 40.0,
            'opt_months': [9, 10, 11, 12]
        },
        'Beetroot': {
            'cat': 'Root Crop', 'base_yield': 5.0, 'season': 'Rabi',
            'temp_mean': 18.5, 'temp_std': 2.0,
            'hum_mean': 67.0, 'hum_std': 5.0,
            'rain_mean': 470.0, 'rain_std': 45.0,
            'opt_months': [10, 11, 12, 1]
        },
        'Ginger': {
            'cat': 'Root Crop', 'base_yield': 3.6, 'season': 'Kharif',
            'temp_mean': 28.5, 'temp_std': 2.5,
            'hum_mean': 82.0, 'hum_std': 5.0,
            'rain_mean': 1250.0, 'rain_std': 100.0,
            'opt_months': [5, 6, 7, 8]
        },
        'Sweet Potato': {
            'cat': 'Root Crop', 'base_yield': 4.8, 'season': 'Kharif',
            'temp_mean': 27.5, 'temp_std': 2.5,
            'hum_mean': 76.0, 'hum_std': 6.0,
            'rain_mean': 920.0, 'rain_std': 80.0,
            'opt_months': [6, 7, 8, 9]
        },

        # Cereals & Grains
        'Rice': {
            'cat': 'Grain', 'base_yield': 3.6, 'season': 'Kharif',
            'temp_mean': 30.0, 'temp_std': 2.5,
            'hum_mean': 84.0, 'hum_std': 5.0,
            'rain_mean': 1350.0, 'rain_std': 120.0,
            'opt_months': [6, 7, 8, 9]
        },
        'Wheat': {
            'cat': 'Grain', 'base_yield': 3.2, 'season': 'Rabi',
            'temp_mean': 15.0, 'temp_std': 2.0,
            'hum_mean': 56.0, 'hum_std': 5.0,
            'rain_mean': 360.0, 'rain_std': 40.0,
            'opt_months': [11, 12, 1, 2]
        },
        'Maize': {
            'cat': 'Grain', 'base_yield': 2.9, 'season': 'Kharif',
            'temp_mean': 26.0, 'temp_std': 2.5,
            'hum_mean': 68.0, 'hum_std': 6.0,
            'rain_mean': 760.0, 'rain_std': 70.0,
            'opt_months': [6, 7, 8, 9]
        }
    }
    
    data = []
    
    for crop, c_info in crops_info.items():
        for _ in range(n_samples_per_crop):
            # Select month predominantly from optimal months
            month = int(np.random.choice(c_info['opt_months']))
            season = c_info['season']
            area = round(float(np.random.uniform(1.0, 10.0)), 2)
            soil_ph = round(float(np.random.uniform(5.8, 7.4)), 2)
            nitrogen = int(np.random.randint(40, 150))
            phosphorus = int(np.random.randint(25, 85))
            potassium = int(np.random.randint(25, 110))
            
            # Weather drawn from crop distribution
            temperature = round(float(np.random.normal(c_info['temp_mean'], c_info['temp_std'])), 1)
            humidity = round(float(np.clip(np.random.normal(c_info['hum_mean'], c_info['hum_std']), 30.0, 95.0)), 1)
            rainfall = round(float(np.clip(np.random.normal(c_info['rain_mean'], c_info['rain_std']), 200.0, 2000.0)), 1)
            
            base_yield = c_info['base_yield']
            ph_factor = 1.0 - abs(soil_ph - 6.5) * 0.08
            npk_factor = (nitrogen * 0.35 + phosphorus * 0.35 + potassium * 0.30) / 100.0
            weather_factor = (temperature / 26.0) * (humidity / 70.0)
            
            yield_val = base_yield * ph_factor * npk_factor * weather_factor + np.random.normal(0, 0.2)
            yield_val = round(max(0.4, float(yield_val)), 2)
            
            data.append({
                'Crop': crop,
                'Category': c_info['cat'],
                'Season': season,
                'Month': month,
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
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)
    df.to_csv(filepath, index=False)
    print(f"[OK] Generated {filepath} with {len(df)} rows across {len(crops_info)} crops.")

def create_sample_disease_images():
    """Generates synthetic leaf images for 12 multi-crop disease classes."""
    categories = [
        'Healthy',
        'Early_Blight',
        'Late_Blight',
        'Powdery_Mildew',
        'Downy_Mildew',
        'Black_Spot',
        'Leaf_Rust',
        'Anthracnose',
        'Bacterial_Leaf_Spot',
        'Leaf_Mold',
        'Root_Rot_Wilt',
        'Mosaic_Virus'
    ]
    base_dir = os.path.join("dataset", "disease")
    
    for cat in categories:
        cat_dir = os.path.join(base_dir, cat)
        os.makedirs(cat_dir, exist_ok=True)
        
        for i in range(20):
            img_path = os.path.join(cat_dir, f"{cat.lower()}_{i+1}.jpg")
            img = Image.new('RGB', (128, 128), color=(34, 139, 34))
            draw = ImageDraw.Draw(img)
            draw.ellipse([15, 10, 113, 118], fill=(46, 139, 87))
            
            if cat == 'Early_Blight':
                draw.ellipse([35, 35, 65, 65], fill=(139, 69, 19))
                draw.ellipse([42, 42, 58, 58], fill=(100, 45, 10))
                draw.ellipse([70, 70, 95, 95], fill=(139, 69, 19))
            elif cat == 'Late_Blight':
                draw.polygon([(30, 30), (75, 20), (65, 80), (20, 60)], fill=(40, 50, 45))
                draw.ellipse([75, 55, 105, 85], fill=(45, 55, 45))
            elif cat == 'Powdery_Mildew':
                draw.ellipse([30, 30, 65, 65], fill=(230, 235, 235))
                draw.ellipse([60, 60, 95, 95], fill=(240, 245, 245))
                draw.ellipse([75, 25, 98, 48], fill=(225, 230, 230))
            elif cat == 'Downy_Mildew':
                draw.polygon([(35, 40), (65, 35), (60, 70), (30, 65)], fill=(205, 190, 60))
                draw.polygon([(65, 60), (95, 55), (90, 90), (60, 85)], fill=(195, 180, 50))
            elif cat == 'Black_Spot':
                draw.ellipse([35, 35, 55, 55], fill=(15, 15, 15))
                draw.ellipse([70, 65, 90, 85], fill=(20, 20, 20))
                draw.ellipse([50, 75, 68, 93], fill=(15, 15, 15))
            elif cat == 'Leaf_Rust':
                draw.ellipse([35, 30, 50, 45], fill=(210, 80, 20))
                draw.ellipse([65, 40, 80, 55], fill=(225, 90, 25))
                draw.ellipse([45, 65, 60, 80], fill=(200, 75, 15))
                draw.ellipse([75, 75, 90, 90], fill=(215, 85, 20))
            elif cat == 'Anthracnose':
                draw.ellipse([35, 35, 65, 65], fill=(85, 40, 15))
                draw.ellipse([42, 42, 58, 58], fill=(170, 130, 90))
                draw.ellipse([70, 65, 95, 90], fill=(85, 40, 15))
            elif cat == 'Bacterial_Leaf_Spot':
                draw.ellipse([30, 30, 60, 60], fill=(220, 200, 30))
                draw.ellipse([38, 38, 52, 52], fill=(60, 30, 15))
                draw.ellipse([65, 65, 95, 95], fill=(220, 200, 30))
                draw.ellipse([73, 73, 87, 87], fill=(60, 30, 15))
            elif cat == 'Leaf_Mold':
                draw.ellipse([30, 45, 80, 95], fill=(180, 155, 35))
            elif cat == 'Root_Rot_Wilt':
                draw.polygon([(15, 10), (45, 20), (40, 100), (15, 118)], fill=(160, 120, 40))
                draw.polygon([(85, 20), (113, 10), (113, 118), (85, 100)], fill=(160, 120, 40))
            elif cat == 'Mosaic_Virus':
                draw.ellipse([25, 25, 55, 55], fill=(185, 225, 60))
                draw.ellipse([65, 35, 95, 65], fill=(140, 195, 50))
                draw.ellipse([40, 65, 70, 95], fill=(195, 235, 70))
                draw.ellipse([75, 70, 105, 100], fill=(150, 205, 55))
            
            img.save(img_path)
            
    print(f"[OK] Created multi-crop sample leaf image dataset under {base_dir} for {len(categories)} disease classes.")

if __name__ == "__main__":
    create_sample_yield_dataset()
    create_sample_disease_images()
