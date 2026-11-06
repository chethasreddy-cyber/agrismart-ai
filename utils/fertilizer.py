import math

# Optimal N-P-K target requirements (kg/acre) and pH ranges for 20 multi-category crops
CROP_NUTRIENT_TARGETS = {
    # Vegetables
    'Tomato':        {'category': 'Vegetable', 'N': 120, 'P': 60, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.0},
    'Potato':        {'category': 'Vegetable', 'N': 150, 'P': 75, 'K': 100, 'min_ph': 5.0, 'max_ph': 6.5},
    'Chilli':        {'category': 'Vegetable', 'N': 100, 'P': 50, 'K': 50, 'min_ph': 6.0, 'max_ph': 7.0},
    'Brinjal':       {'category': 'Vegetable', 'N': 110, 'P': 50, 'K': 50, 'min_ph': 5.5, 'max_ph': 6.8},
    'Cabbage':       {'category': 'Vegetable', 'N': 140, 'P': 60, 'K': 80, 'min_ph': 6.0, 'max_ph': 7.2},
    'Cucumber':      {'category': 'Vegetable', 'N': 80,  'P': 40, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.5},
    'Onion':         {'category': 'Vegetable', 'N': 100, 'P': 50, 'K': 80, 'min_ph': 6.0, 'max_ph': 7.0},

    # Flowers
    'Rose':          {'category': 'Flower',    'N': 80,  'P': 40, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.0},
    'Marigold':      {'category': 'Flower',    'N': 90,  'P': 50, 'K': 50, 'min_ph': 6.2, 'max_ph': 7.5},
    'Jasmine':       {'category': 'Flower',    'N': 60,  'P': 40, 'K': 40, 'min_ph': 6.5, 'max_ph': 7.5},
    'Sunflower':     {'category': 'Flower',    'N': 70,  'P': 50, 'K': 40, 'min_ph': 6.0, 'max_ph': 7.5},
    'Chrysanthemum': {'category': 'Flower',    'N': 85,  'P': 45, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.0},

    # Root & Tuber Crops
    'Carrot':        {'category': 'Root Crop', 'N': 90,  'P': 45, 'K': 80, 'min_ph': 5.8, 'max_ph': 6.8},
    'Radish':        {'category': 'Root Crop', 'N': 80,  'P': 40, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.0},
    'Beetroot':      {'category': 'Root Crop', 'N': 85,  'P': 45, 'K': 70, 'min_ph': 6.0, 'max_ph': 7.5},
    'Ginger':        {'category': 'Root Crop', 'N': 100, 'P': 50, 'K': 100, 'min_ph': 5.5, 'max_ph': 6.5},
    'Sweet Potato':  {'category': 'Root Crop', 'N': 75,  'P': 40, 'K': 90, 'min_ph': 5.5, 'max_ph': 6.8},

    # Cereals & Grains
    'Rice':          {'category': 'Grain',     'N': 100, 'P': 50, 'K': 50, 'min_ph': 5.5, 'max_ph': 6.8},
    'Wheat':         {'category': 'Grain',     'N': 120, 'P': 40, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.5},
    'Maize':         {'category': 'Grain',     'N': 120, 'P': 60, 'K': 40, 'min_ph': 5.8, 'max_ph': 7.0}
}

def calculate_fertilizer_recommendation(crop, soil_n, soil_p, soil_k, soil_ph, area_acres=1.0):
    """
    Calculates exact fertilizer deficits and recommends Urea, DAP, and MOP dosages.
    
    Fertilizer Nutrient Contents:
      - Urea: 46% Nitrogen
      - DAP (Di-Ammonium Phosphate): 18% Nitrogen, 46% Phosphorus
      - MOP (Muriate of Potash): 60% Potassium
    """
    targets = CROP_NUTRIENT_TARGETS.get(crop, CROP_NUTRIENT_TARGETS['Tomato'])
    
    # Calculate Nutrient Deficit (kg/acre)
    deficit_n = max(0.0, float(targets['N'] - soil_n))
    deficit_p = max(0.0, float(targets['P'] - soil_p))
    deficit_k = max(0.0, float(targets['K'] - soil_k))
    
    # Calculate DAP needed for Phosphorus deficit
    # DAP provides 46% P and 18% N
    dap_per_acre = deficit_p / 0.46 if deficit_p > 0 else 0.0
    n_from_dap = dap_per_acre * 0.18
    
    # Remaining Nitrogen deficit after DAP
    remaining_n_deficit = max(0.0, deficit_n - n_from_dap)
    urea_per_acre = remaining_n_deficit / 0.46 if remaining_n_deficit > 0 else 0.0
    
    # Calculate MOP needed for Potassium deficit
    mop_per_acre = deficit_k / 0.60 if deficit_k > 0 else 0.0
    
    # Scale total for farm area
    total_urea = round(urea_per_acre * area_acres, 1)
    total_dap = round(dap_per_acre * area_acres, 1)
    total_mop = round(mop_per_acre * area_acres, 1)

    # Soil pH Amendment Advice
    ph_advice = f"Soil pH {soil_ph:.1f} is in the optimal range ({targets['min_ph']} - {targets['max_ph']}) for {crop}."
    if soil_ph < targets['min_ph']:
        ph_advice = f"Soil is acidic (pH {soil_ph:.1f}). Apply Agricultural Lime (Calcium Carbonate) at ~200-300 kg/acre to raise pH toward {targets['min_ph']}."
    elif soil_ph > targets['max_ph']:
        ph_advice = f"Soil is alkaline (pH {soil_ph:.1f}). Apply Elemental Sulfur or Gypsum at ~100-200 kg/acre to lower pH toward {targets['max_ph']}."

    return {
        'crop': crop,
        'category': targets.get('category', 'Crop'),
        'area_acres': area_acres,
        'soil_ph': soil_ph,
        'deficits': {
            'N': round(deficit_n, 1),
            'P': round(deficit_p, 1),
            'K': round(deficit_k, 1)
        },
        'per_acre': {
            'Urea_kg': round(urea_per_acre, 1),
            'DAP_kg': round(dap_per_acre, 1),
            'MOP_kg': round(mop_per_acre, 1)
        },
        'total_farm': {
            'Urea_kg': total_urea,
            'DAP_kg': total_dap,
            'MOP_kg': total_mop
        },
        'ph_advice': ph_advice
    }

if __name__ == "__main__":
    rec = calculate_fertilizer_recommendation('Rose', soil_n=50, soil_p=20, soil_k=30, soil_ph=6.5, area_acres=2.0)
    print("=" * 60)
    print("FERTILIZER RECOMMENDATION ENGINE TEST (20 CROPS)")
    print("=" * 60)
    print(f"Crop: {rec['crop']} ({rec['category']}) | Farm Area: {rec['area_acres']} acres | Soil pH: {rec['soil_ph']}")
    print(f"Nutrient Deficits (kg/acre): N: {rec['deficits']['N']}, P: {rec['deficits']['P']}, K: {rec['deficits']['K']}")
    print(f"  • Urea (46% N) : {rec['total_farm']['Urea_kg']} kg")
    print(f"  • DAP (46% P)  : {rec['total_farm']['DAP_kg']} kg")
    print(f"  • MOP (60% K)  : {rec['total_farm']['MOP_kg']} kg")
    print(f"pH Advice: {rec['ph_advice']}")
    print("=" * 60)
