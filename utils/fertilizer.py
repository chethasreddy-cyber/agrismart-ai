import math

# Optimal N-P-K target requirements (kg/acre) and pH ranges for common crops
CROP_NUTRIENT_TARGETS = {
    'Tomato': {'N': 120, 'P': 60, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.0},
    'Potato': {'N': 150, 'P': 75, 'K': 100, 'min_ph': 5.0, 'max_ph': 6.5},
    'Rice':   {'N': 100, 'P': 50, 'K': 50, 'min_ph': 5.5, 'max_ph': 6.8},
    'Wheat':  {'N': 120, 'P': 40, 'K': 60, 'min_ph': 6.0, 'max_ph': 7.5},
    'Maize':  {'N': 120, 'P': 60, 'K': 40, 'min_ph': 5.8, 'max_ph': 7.0}
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
    ph_advice = "Soil pH is in the optimal range."
    if soil_ph < targets['min_ph']:
        ph_advice = f"Soil is acidic (pH {soil_ph:.1f}). Apply Agricultural Lime (Calcium Carbonate) at ~200-300 kg/acre to raise pH to {targets['min_ph']}."
    elif soil_ph > targets['max_ph']:
        ph_advice = f"Soil is alkaline (pH {soil_ph:.1f}). Apply Elemental Sulfur or Gypsum at ~100-200 kg/acre to lower pH to {targets['max_ph']}."

    return {
        'crop': crop,
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
    rec = calculate_fertilizer_recommendation('Tomato', soil_n=80, soil_p=30, soil_k=40, soil_ph=5.8, area_acres=2.5)
    print("=" * 60)
    print("SMART FERTILIZER RECOMMENDATION ENGINE TEST")
    print("=" * 60)
    print(f"Crop: {rec['crop']} | Farm Area: {rec['area_acres']} acres | Soil pH: {rec['soil_ph']}")
    print(f"Nutrient Deficits (kg/acre): N: {rec['deficits']['N']}, P: {rec['deficits']['P']}, K: {rec['deficits']['K']}")
    print("Recommended Fertilizer Dosage (Total Farm):")
    print(f"  • Urea (46% N) : {rec['total_farm']['Urea_kg']} kg")
    print(f"  • DAP (46% P)  : {rec['total_farm']['DAP_kg']} kg")
    print(f"  • MOP (60% K)  : {rec['total_farm']['MOP_kg']} kg")
    print(f"pH Advice: {rec['ph_advice']}")
    print("=" * 60)
