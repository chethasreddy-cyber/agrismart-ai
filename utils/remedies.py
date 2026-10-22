def get_crop_remedies(disease_name):
    """
    Returns curated Organic vs. Chemical remedies for the detected disease.
    """
    normalized = disease_name.lower().replace(' ', '_').replace('-', '_')

    remedies = {
        'early_blight': {
            'disease': 'Early Blight (Alternaria solani)',
            'symptoms': 'Concentric dark ring target-spots with yellow halo on older leaves.',
            'organic': {
                'title': 'Cold-Pressed Neem Oil (3%) + Trichoderma Viride',
                'badge': '🌿 100% Certified Organic',
                'action_type': 'Bio-Fungicide & Systemic Immunity Booster',
                'eco_score': 95,
                'cost_per_acre': '₹350 – ₹450',
                'phi_days': '0 Days (Harvest safe immediately)',
                'bee_safety': 'Safe for pollinators & honeybees',
                'ingredients': 'Azadirachtin (1500 PPM), Trichoderma spores, Potassium Bicarbonate',
                'dosage': '5 ml Neem Oil + 2g Trichoderma per 1 Litre water',
                'schedule': 'Spray every 7–10 days in early morning or after 4 PM.',
                'soil_benefit': 'Enriches soil beneficial microflora and strengthens root defense.'
            },
            'chemical': {
                'title': 'Mancozeb 75% WP + Metalaxyl 8% (Ridomil MZ)',
                'badge': '⚗️ Synthetic Fast-Knockdown',
                'action_type': 'Broad-Spectrum Protective & Curative Fungicide',
                'eco_score': 35,
                'cost_per_acre': '₹680 – ₹850',
                'phi_days': '7 – 10 Days before picking fruit',
                'bee_safety': 'Moderate risk — avoid spraying during active bloom',
                'ingredients': 'Dithiocarbamate + Phenylamide chemical compounds',
                'dosage': '2.5 g per 1 Litre clean water with protective gloves & mask',
                'schedule': 'Maximum 2 sprays at 12–14 day intervals.',
                'soil_benefit': 'Synthetic chemical residue; requires strict adherence to safety interval.'
            }
        },
        'late_blight': {
            'disease': 'Late Blight (Phytophthora infestans)',
            'symptoms': 'Water-soaked dark lesions with white fungal mold under humid conditions.',
            'organic': {
                'title': 'Bordeaux Mixture (1%) + Pseudomonas fluorescens',
                'badge': '🌿 Organic Mineral & Bio-Fungicide',
                'action_type': 'Preventative Protective Barrier',
                'eco_score': 88,
                'cost_per_acre': '₹400 – ₹500',
                'phi_days': '1 Day',
                'bee_safety': 'Safe when sprayed in early morning',
                'ingredients': 'Copper Sulphate + Slaked Lime + Beneficial bacterial culture',
                'dosage': '10 g Copper Sulphate + 10 g Lime in 1 Litre water',
                'schedule': 'Thorough canopy drenching, especially undersides of leaves.',
                'soil_benefit': 'Supplies essential copper micronutrient without toxic buildup.'
            },
            'chemical': {
                'title': 'Cymoxanil 8% + Mancozeb 64% WP (Curzate)',
                'badge': '⚗️ High-Potency Systemic',
                'action_type': 'Penetrating Curative with Post-Infection Stop Action',
                'eco_score': 30,
                'cost_per_acre': '₹850 – ₹1,100',
                'phi_days': '10 – 14 Days waiting period',
                'bee_safety': 'Harmful to aquatic life & bees during spray window',
                'ingredients': 'Aliphatic nitrogen derivative + Manganese/Zinc bisdithiocarbamate',
                'dosage': '3 g per 1 Litre water with full PPE equipment',
                'schedule': 'Spray immediately at lesion onset; rotate with non-cross-resistant chemistry.',
                'soil_benefit': 'High chemical persistence; flush spray equipment away from water sources.'
            }
        },
        'leaf_mold': {
            'disease': 'Leaf Mold (Passalora fulva)',
            'symptoms': 'Pale green or yellowish spots on upper leaf with olive-brown velvety mold underneath.',
            'organic': {
                'title': 'Potassium Bicarbonate Buffer + Horticultural Herbal Oil',
                'badge': '🌿 Food-Grade Eco Solution',
                'action_type': 'pH Disruption & Fungal Cell Dehydration',
                'eco_score': 96,
                'cost_per_acre': '₹280 – ₹380',
                'phi_days': '0 Days (No chemical withholding)',
                'bee_safety': '100% Non-toxic to pollinators and domestic animals',
                'ingredients': 'Food-grade Potassium Bicarbonate + Cold-pressed vegetable oils',
                'dosage': '4 g Potassium Bicarbonate + 3 ml vegetable oil per 1 Litre water',
                'schedule': 'Spray weekly; increase airflow between crop rows by pruning lower foliage.',
                'soil_benefit': 'Breaks down into potassium ions that nourish soil fertility.'
            },
            'chemical': {
                'title': 'Difenoconazole 25% EC (Score Fungicide)',
                'badge': '⚗️ Triazole Systemic',
                'action_type': 'Sterol Demethylation Inhibitor (DMI)',
                'eco_score': 42,
                'cost_per_acre': '₹720 – ₹900',
                'phi_days': '5 – 7 Days',
                'bee_safety': 'Do not apply near flowering weeds or hives',
                'ingredients': 'Difenoconazole active ingredient',
                'dosage': '0.5 ml per 1 Litre water',
                'schedule': 'Apply twice per growing season at 14-day intervals.',
                'soil_benefit': 'Moderate persistence; avoid soil over-drenching.'
            }
        }
    }

    # Default fallback for healthy or unclassified
    default_remedy = {
        'disease': 'General Crop Health Maintenance',
        'symptoms': 'Crop canopy shows normal vigor with minimal or no pathogenic spots.',
        'organic': {
            'title': 'Enriched Vermicompost Tea & Bio-NPK Consortium',
            'badge': '🌿 Organic Vitality Booster',
            'action_type': 'Preventative Foliar & Root Microbiome Shield',
            'eco_score': 100,
            'cost_per_acre': '₹220 – ₹300',
            'phi_days': '0 Days',
            'bee_safety': 'Completely pollinator friendly',
            'ingredients': 'Humic substances, Azotobacter, PSB, Seaweed amino acids',
            'dosage': '20 ml Vermiwash or 2 g Bio-consortium per 1 Litre water',
            'schedule': 'Spray every 15 days to maintain disease immunity.',
            'soil_benefit': 'Enhances organic carbon and stimulates earthworm activity.'
        },
        'chemical': {
            'title': 'Water-Soluble 19-19-19 Balanced Micronutrient Foliar',
            'badge': '⚗️ Synthetic Growth Enhancer',
            'action_type': 'Direct Mineral Supplementation',
            'eco_score': 65,
            'cost_per_acre': '₹400 – ₹550',
            'phi_days': '2 Days',
            'bee_safety': 'Low toxicity to pollinators',
            'ingredients': 'Refined Nitrogen, Phosphate, Potash with Chelated Zinc & Iron',
            'dosage': '5 g per 1 Litre water',
            'schedule': 'Apply early morning during active vegetative or flowering stage.',
            'soil_benefit': 'Rapid plant absorption with minimal soil accumulation.'
        }
    }

    for key, val in remedies.items():
        if key in normalized:
            return val

    return default_remedy
