def get_crop_remedies(disease_name):
    """
    Returns curated Organic vs. Chemical remedies for all major plant diseases
    spanning flowers, vegetables, root crops, and grains.
    """
    name_clean = disease_name.lower().replace('-', '_').replace(' ', '_').strip()

    remedies = {
        'early_blight': {
            'disease': 'Early Blight (Alternaria solani / alternata)',
            'symptoms': 'Concentric dark target-rings with chlorotic yellow halo on older leaves of vegetables and flowers.',
            'affected_crops': 'Tomato, Potato, Brinjal, Chilli, Cabbage, Marigold',
            'organic': {
                'title': 'Cold-Pressed Neem Oil (3%) + Trichoderma viride',
                'badge': '🌿 100% Certified Organic',
                'action_type': 'Bio-Fungicide & Systemic Immunity Booster',
                'eco_score': 95,
                'cost_per_acre': '₹350 – ₹450',
                'phi_days': '0 Days (Harvest safe immediately)',
                'bee_safety': 'Safe for pollinators & beneficial insects',
                'ingredients': 'Azadirachtin (1500 PPM), Trichoderma viride bio-spores, Potassium Bicarbonate',
                'dosage': '5 ml Neem Oil + 2.5 g Trichoderma per 1 Litre water',
                'schedule': 'Spray every 7–10 days in early morning or after 4 PM.',
                'soil_benefit': 'Enriches beneficial rhizobacteria and suppresses soil-borne fungal spores.'
            },
            'chemical': {
                'title': 'Mancozeb 75% WP + Metalaxyl 8% (Ridomil MZ)',
                'badge': '⚗️ Fast-Knockdown Synthetic',
                'action_type': 'Contact + Systemic Protective & Curative Fungicide',
                'eco_score': 35,
                'cost_per_acre': '₹680 – ₹850',
                'phi_days': '7 – 10 Days before picking fruit',
                'bee_safety': 'Moderate risk — avoid spraying during peak flower bloom',
                'ingredients': 'Dithiocarbamate + Phenylamide chemical compounds',
                'dosage': '2.5 g per 1 Litre clean water with protective PPE',
                'schedule': 'Maximum 2 sprays at 12–14 day intervals.',
                'soil_benefit': 'Synthetic chemical residue; flush spray nozzles away from water channels.'
            }
        },
        'late_blight': {
            'disease': 'Late Blight (Phytophthora infestans)',
            'symptoms': 'Rapidly expanding water-soaked greasy brown lesions with white fuzzy sporulation under high humidity.',
            'affected_crops': 'Potato, Tomato, Chilli, Brinjal',
            'organic': {
                'title': 'Bordeaux Mixture (1%) + Pseudomonas fluorescens',
                'badge': '🌿 Mineral & Biological Barrier',
                'action_type': 'Multi-Site Protective Surface Shield',
                'eco_score': 88,
                'cost_per_acre': '₹400 – ₹520',
                'phi_days': '1 Day',
                'bee_safety': 'Safe when applied before sunrise',
                'ingredients': 'Copper Sulphate + Hydrated Lime + Beneficial antagonistic bacteria',
                'dosage': '10 g Copper Sulphate + 10 g Lime in 1 Litre water',
                'schedule': 'Thorough canopy drenching, especially undersides of lower leaves.',
                'soil_benefit': 'Supplies essential copper micronutrient without toxic synthetic buildup.'
            },
            'chemical': {
                'title': 'Cymoxanil 8% + Mancozeb 64% WP (Curzate Fungicide)',
                'badge': '⚗️ High-Potency Curative',
                'action_type': 'Penetrating Systemic with Post-Infection Stop Action',
                'eco_score': 30,
                'cost_per_acre': '₹850 – ₹1,100',
                'phi_days': '10 – 14 Days waiting period',
                'bee_safety': 'Toxic to aquatic life & pollinators during wet spray film',
                'ingredients': 'Aliphatic nitrogen derivative + Bisdithiocarbamate',
                'dosage': '3.0 g per 1 Litre water with protective equipment',
                'schedule': 'Apply immediately at lesion onset; repeat in 10 days if humid weather persists.',
                'soil_benefit': 'Strict adherence to withholding interval required.'
            }
        },
        'powdery_mildew': {
            'disease': 'Powdery Mildew (Podosphaera pannosa / Erysiphe cichoracearum)',
            'symptoms': 'White powdery talc-like patches covering leaves, stems, and flower buds, causing curling and stunted blooms.',
            'affected_crops': 'Rose, Marigold, Cucumber, Cabbage, Tomato, Sunflower, Chrysanthemum',
            'organic': {
                'title': 'Potassium Bicarbonate + Horticultural Neem Emulsion',
                'badge': '🌿 Organic Mineral Fungicide',
                'action_type': 'Cellular Osmotic Shock & Fungal Wall Disruption',
                'eco_score': 96,
                'cost_per_acre': '₹300 – ₹420',
                'phi_days': '0 Days (No chemical withholding)',
                'bee_safety': 'Completely harmless to pollinators and ladybugs',
                'ingredients': 'Food-grade Potassium Bicarbonate (4g/L) + Cold-pressed Neem oil (3ml/L)',
                'dosage': '4 g Potassium Bicarbonate + 3 ml Neem Oil per 1 Litre water',
                'schedule': 'Spray every 5–7 days in morning. Improve air spacing between plants.',
                'soil_benefit': 'Breaks down into bio-available potassium nutrition for root health.'
            },
            'chemical': {
                'title': 'Hexaconazole 5% SC / Difenoconazole 25% EC (Contaf / Score)',
                'badge': '⚗️ Triazole Systemic',
                'action_type': 'Ergosterol Biosynthesis Inhibitor (EBI)',
                'eco_score': 38,
                'cost_per_acre': '₹550 – ₹750',
                'phi_days': '7 Days',
                'bee_safety': 'Do not spray during midday active bee visits',
                'ingredients': 'Hexaconazole systemic triazole fungicide',
                'dosage': '1.5 ml to 2 ml per 1 Litre water',
                'schedule': 'Spray at first visible white speckle; repeat once after 12 days if needed.',
                'soil_benefit': 'Synthetic fungicide; limit to maximum 2 applications per crop cycle.'
            }
        },
        'downy_mildew': {
            'disease': 'Downy Mildew (Pseudoperonospora cubensis / Peronospora)',
            'symptoms': 'Angular yellow chlorotic lesions bounded by leaf veins on top surface, with purple-grey downy growth underneath.',
            'affected_crops': 'Cucumber, Cabbage, Onion, Radish, Rose',
            'organic': {
                'title': 'Copper Hydroxide Bio-Shield + Bacillus subtilis',
                'badge': '🌿 Organic Microbial & Copper Protective',
                'action_type': 'Spore Germination Inhibitor',
                'eco_score': 90,
                'cost_per_acre': '₹380 – ₹490',
                'phi_days': '1 Day',
                'bee_safety': 'Safe for pollinators',
                'ingredients': 'OMRI-listed Copper Hydroxide + Bacillus subtilis QST 713 bio-strain',
                'dosage': '2 g Copper Hydroxide + 2 ml Bacillus suspension per 1 Litre water',
                'schedule': 'Spray preventively during foggy/dew-heavy mornings every 7 days.',
                'soil_benefit': 'Bacillus colonizes plant phyllosphere and triggers systemic acquired resistance.'
            },
            'chemical': {
                'title': 'Dimethomorph 50% WP (Acrobat Fungicide)',
                'badge': '⚗️ Oomycete-Specific Curative',
                'action_type': 'Cell Wall Biosynthesis Disruptor',
                'eco_score': 32,
                'cost_per_acre': '₹750 – ₹980',
                'phi_days': '7 – 10 Days',
                'bee_safety': 'Moderate hazard during application window',
                'ingredients': 'Cinnamic acid amide derivative (Dimethomorph)',
                'dosage': '1.5 g per 1 Litre water with surfactant sticker',
                'schedule': 'Apply 2 rounds at 10-day intervals upon first angular lesion appearance.',
                'soil_benefit': 'Wash spray tanks away from groundwater wells.'
            }
        },
        'black_spot': {
            'disease': 'Black Spot (Diplocarpon rosae / Alternaria brassicae)',
            'symptoms': 'Circular black lesions with feathery fringed margins followed by leaf yellowing and severe premature defoliation.',
            'affected_crops': 'Rose, Marigold, Cabbage, Radish, Chrysanthemum',
            'organic': {
                'title': 'Baking Soda Buffer + Garlic & Neem Extract Foliar',
                'badge': '🌿 Organic Botanical Fungiphobe',
                'action_type': 'Surface pH Alkaline Shift & Antifungal Allicin Action',
                'eco_score': 94,
                'cost_per_acre': '₹250 – ₹350',
                'phi_days': '0 Days',
                'bee_safety': '100% Eco-safe',
                'ingredients': 'Sodium Bicarbonate + Crushed Garlic extract + Neem Azadirachtin',
                'dosage': '3 g Baking Soda + 5 ml Garlic-Neem extract in 1 Litre water',
                'schedule': 'Spray every 5 days; prune and destroy infected fallen bottom leaves.',
                'soil_benefit': 'Prevents overwintering fungal ascocarps from harboring in soil mulch.'
            },
            'chemical': {
                'title': 'Propiconazole 25% EC (Tilt Fungicide)',
                'badge': '⚗️ Broad-Spectrum Triazole',
                'action_type': 'Systemic Sterol Inhibitor with Acropetal Translocation',
                'eco_score': 36,
                'cost_per_acre': '₹620 – ₹820',
                'phi_days': '14 Days for edible crops; ornamental safe',
                'bee_safety': 'Toxic to aquatic organisms; spray in late evening',
                'ingredients': 'Propiconazole active ingredient',
                'dosage': '1.0 ml per 1 Litre clean water',
                'schedule': 'Spray at onset of feathery spots; maximum 2 applications per season.',
                'soil_benefit': 'Moderate environmental persistence.'
            }
        },
        'leaf_rust': {
            'disease': 'Leaf Rust (Puccinia recondita / Puccinia chrysanthemi)',
            'symptoms': 'Small, raised reddish-orange or cinnamon-brown pustules that rupture leaf epidermis releasing powdery rust spores.',
            'affected_crops': 'Wheat, Rose, Sunflower, Chrysanthemum, Maize, Beans',
            'organic': {
                'title': 'Wettable Micronized Sulphur (80% WDG) + Cow Urine (5%)',
                'badge': '🌿 Natural Mineral & Organic Repellent',
                'action_type': 'Multi-Site Spore Dehydrator & Foliar Immunizer',
                'eco_score': 89,
                'cost_per_acre': '₹290 – ₹380',
                'phi_days': '1 Day',
                'bee_safety': 'Safe when sprayed below 32°C ambient temperature',
                'ingredients': 'Elemental Micronized Sulphur + Fermented Cow Urine bio-extract',
                'dosage': '2.5 g Micronized Sulphur in 1 Litre water',
                'schedule': 'Spray uniformly over canopy; do not spray under scorching direct sun.',
                'soil_benefit': 'Provides essential elemental sulphur fertilizer for chlorophyll synthesis.'
            },
            'chemical': {
                'title': 'Tebuconazole 25.9% EC (Folicur Fungicide)',
                'badge': '⚗️ High-Efficacy Systemic Curative',
                'action_type': 'Demethylation Inhibitor Stopping Rust Pustule Sporulation',
                'eco_score': 34,
                'cost_per_acre': '₹700 – ₹920',
                'phi_days': '15 Days for cereals / grains',
                'bee_safety': 'Moderate risk — avoid spray drift near apiaries',
                'ingredients': 'Tebuconazole broad-spectrum triazole',
                'dosage': '1.5 ml per 1 Litre water',
                'schedule': '1 application at flag leaf emergence or first rust pustule sighting.',
                'soil_benefit': 'High field efficacy; strictly observe pre-harvest safety interval.'
            }
        },
        'anthracnose': {
            'disease': 'Anthracnose (Colletotrichum gloeosporioides / capsici)',
            'symptoms': 'Sunken circular dark necrotic lesions with concentric salmon-pink spore masses in center, causing fruit rot and twig dieback.',
            'affected_crops': 'Chilli, Tomato, Jasmine, Rose, Ginger, Brinjal',
            'organic': {
                'title': 'Pseudomonas fluorescens + Bio-Copper Bordeaux Emulsion',
                'badge': '🌿 Bio-Control Microbial Shield',
                'action_type': 'Antagonistic Siderophore & Secondary Metabolite Production',
                'eco_score': 92,
                'cost_per_acre': '₹340 – ₹450',
                'phi_days': '0 Days',
                'bee_safety': 'Pollinator friendly',
                'ingredients': 'Pseudomonas fluorescens (1x10^8 CFU/g) + Copper Octanoate',
                'dosage': '5 g Pseudomonas + 3 ml Copper Octanoate in 1 Litre water',
                'schedule': 'Spray at early vegetative and flowering stages at 10-day intervals.',
                'soil_benefit': 'Aggressively outcompetes fungal resting structures in root rhizosphere.'
            },
            'chemical': {
                'title': 'Azoxystrobin 18.2% + Difenoconazole 11.4% SC (Amistar Top)',
                'badge': '⚗️ Dual-Action Strobilurin & Triazole',
                'action_type': 'Mitochondrial Respiration Inhibitor + Sterol Disruptor',
                'eco_score': 31,
                'cost_per_acre': '₹950 – ₹1,250',
                'phi_days': '5 – 7 Days',
                'bee_safety': 'Hazardous to bees while liquid spray is wet',
                'ingredients': 'QoI Strobilurin + DMI Triazole combination',
                'dosage': '1.0 ml per 1 Litre water',
                'schedule': 'Spray immediately at fruit spot initiation; repeat once after 14 days.',
                'soil_benefit': 'Systemic translaminar action protecting both new shoots and developing pods.'
            }
        },
        'bacterial_leaf_spot': {
            'disease': 'Bacterial Leaf Spot (Xanthomonas campestris / vesicatoria)',
            'symptoms': 'Small, angular water-soaked dark brown spots with prominent translucent yellow halos, tearing leaf margins.',
            'affected_crops': 'Chilli, Tomato, Cabbage, Radish, Jasmine, Marigold',
            'organic': {
                'title': 'Streptomyces lydicus + Copper Oxychloride (50% WP)',
                'badge': '🌿 Organic Mineral & Actinomycete Blend',
                'action_type': 'Bacteriostatic Mineral Membrane Disruption',
                'eco_score': 87,
                'cost_per_acre': '₹320 – ₹420',
                'phi_days': '2 Days',
                'bee_safety': 'Low hazard when dry',
                'ingredients': 'Copper Oxychloride (COC) + Beneficial bio-actinomycete spores',
                'dosage': '2.5 g Copper Oxychloride per 1 Litre water',
                'schedule': 'Spray preventively before rainy spells. Avoid overhead sprinkler irrigation.',
                'soil_benefit': 'Reduces bacterial splash dispersal between neighboring crop beds.'
            },
            'chemical': {
                'title': 'Streptocycline (90% Streptomycin + 10% Tetracycline) + COC',
                'badge': '⚗️ Agricultural Antibacterial Complex',
                'action_type': 'Bacterial 30S Ribosome Protein Synthesis Blocker',
                'eco_score': 28,
                'cost_per_acre': '₹480 – ₹650',
                'phi_days': '14 Days',
                'bee_safety': 'Harmful to pollinators; spray only after sunset',
                'ingredients': 'Streptomycin sulphate + Tetracycline hydrochloride',
                'dosage': '1 g Streptocycline pouch per 10 Litres water combined with 20g COC',
                'schedule': 'Maximum 2 sprays 10 days apart; do not overuse to prevent bacterial resistance.',
                'soil_benefit': 'Strict dosage observance required to prevent antibiotic residue accumulation.'
            }
        },
        'leaf_mold': {
            'disease': 'Leaf Mold (Passalora fulva / Cladosporium)',
            'symptoms': 'Diffuse pale yellow chlorotic spots on upper leaf with velvety olive-brown mold cushions underneath.',
            'affected_crops': 'Tomato, Brinjal, Chilli, Greenhouse Flowers & Vegetables',
            'organic': {
                'title': 'Potassium Bicarbonate + Bio-Trichoderma Harzianum',
                'badge': '🌿 Food-Grade Eco Solution',
                'action_type': 'Spore Lysis & Foliar Microclimate Deacidification',
                'eco_score': 96,
                'cost_per_acre': '₹280 – ₹380',
                'phi_days': '0 Days (No chemical withholding)',
                'bee_safety': '100% Non-toxic to bees, animals, and beneficial fauna',
                'ingredients': 'Food-grade Potassium Bicarbonate + Trichoderma harzianum spores',
                'dosage': '4 g Potassium Bicarbonate + 3 g Trichoderma per 1 Litre water',
                'schedule': 'Spray weekly; prune bottom dense suckers to ensure vigorous air circulation.',
                'soil_benefit': 'Nutrient potassium breakdown enriches soil micro-elements.'
            },
            'chemical': {
                'title': 'Chlorothalonil 75% WP (Kavach Fungicide)',
                'badge': '⚗️ Multi-Site Contact Protectant',
                'action_type': 'Fungal Thiol Binding & Enzyme Deactivator',
                'eco_score': 40,
                'cost_per_acre': '₹650 – ₹850',
                'phi_days': '7 Days',
                'bee_safety': 'Do not apply near flowering weeds',
                'ingredients': 'Chlorothalonil organochlorine fungicide',
                'dosage': '2.0 g per 1 Litre water',
                'schedule': 'Spray thoroughly covering lower canopy foliage every 10–14 days.',
                'soil_benefit': 'Binds tightly to leaf cuticle with excellent rain-fastness.'
            }
        },
        'root_rot_wilt': {
            'disease': 'Root Rot & Fusarium Vascular Wilt (Fusarium oxysporum / Pythium)',
            'symptoms': 'Lower foliage yellowing, vascular brown browning inside stem, stunted tubers/roots, and sudden midday plant wilting.',
            'affected_crops': 'Carrot, Radish, Beetroot, Ginger, Sweet Potato, Potato, Tomato, Rose',
            'organic': {
                'title': 'Trichoderma asperellum + VAM (Mycorrhiza) Root Drench',
                'badge': '🌿 Bio-Fungicide & Root Colonizer',
                'action_type': 'Root Shielding & Hyperparasitic Mycelial Destruction',
                'eco_score': 98,
                'cost_per_acre': '₹420 – ₹550',
                'phi_days': '0 Days',
                'bee_safety': 'Completely harmless to bees and earthworms',
                'ingredients': 'Trichoderma asperellum (2x10^9 CFU) + Glomus intraradices mycorrhiza',
                'dosage': '10 g Trichoderma + 10 g VAM per 1 Litre water drenched into root zone',
                'schedule': 'Drench seedling base at planting and repeat 20 days later. Avoid waterlogging.',
                'soil_benefit': 'Dramatically improves root phosphorus absorption and restores soil health.'
            },
            'chemical': {
                'title': 'Carbendazim 12% + Mancozeb 63% WP (Saaf Fungicide)',
                'badge': '⚗️ Systemic + Contact Dual Fungicide',
                'action_type': 'Tubulin Beta-Chain Polymerization Inhibitor',
                'eco_score': 33,
                'cost_per_acre': '₹580 – ₹780',
                'phi_days': '14 – 21 Days',
                'bee_safety': 'Do not contaminate irrigation runoff',
                'ingredients': 'Benzimidazole + Dithiocarbamate chemistry',
                'dosage': '2.0 g per 1 Litre water drenched around root collar (150 ml per plant)',
                'schedule': 'Immediate root drench upon detecting early wilt symptoms in patch.',
                'soil_benefit': 'Chemical active residues; adhere strictly to pre-harvest intervals.'
            }
        },
        'mosaic_virus': {
            'disease': 'Mosaic Virus (Tobacco / Cucumber / Chilli Mosaic Virus)',
            'symptoms': 'Mottled dark and light green mosaic mosaic blisters, leaf puckering, vein clearing, and severe bush stunting.',
            'affected_crops': 'Tomato, Chilli, Cucumber, Rose, Marigold, Potato',
            'organic': {
                'title': 'Yellow Sticky Traps + Cold-Pressed Neem Oil (10,000 PPM) + Milk Protein',
                'badge': '🌿 Organic Vector Control & Protein Barrier',
                'action_type': 'Aphid/Whitefly Vector Suppression & Viral Capsid Inactivation',
                'eco_score': 97,
                'cost_per_acre': '₹350 – ₹480',
                'phi_days': '0 Days',
                'bee_safety': '100% Pollinator Safe',
                'ingredients': 'Neem Azadirachtin + Raw milk lactoferrin (10% foliar spray)',
                'dosage': '5 ml Neem Oil + 100 ml Fresh Milk per 1 Litre water',
                'schedule': 'Install 15 yellow sticky traps per acre; spray weekly to kill insect vectors. Rogue out infected plants.',
                'soil_benefit': 'Maintains natural predator-prey balance in the agricultural ecosystem.'
            },
            'chemical': {
                'title': 'Thiamethoxam 25% WG / Acetamiprid 20% SP (Insect Vector Control)',
                'badge': '⚗️ Systemic Neonicotinoid Vector Control',
                'action_type': 'Nicotinic Acetylcholine Receptor Blocker for Sucking Pests',
                'eco_score': 30,
                'cost_per_acre': '₹550 – ₹720',
                'phi_days': '7 – 10 Days',
                'bee_safety': 'HIGH RISK — Do not spray on blooming crops or near beehives',
                'ingredients': 'Thiamethoxam systemic insecticide targeting aphids, thrips, whiteflies',
                'dosage': '0.5 g per 1 Litre water',
                'schedule': 'Apply once when sucking vector population crosses economic threshold (ETL).',
                'soil_benefit': 'Persistent neonicotinoid; use strictly according to label guidelines.'
            }
        }
    }

    # Healthy fallback
    healthy_remedy = {
        'disease': 'Healthy Plant Canopy (Optimal Vigor)',
        'symptoms': 'Foliage exhibits vigorous chlorophyll green coloration, crisp margins, and no visible necrotic lesions.',
        'affected_crops': 'All Varieties (Vegetables, Flowers, Root Crops, Grains)',
        'organic': {
            'title': 'Enriched Vermicompost Tea & Bio-NPK Microbial Consortium',
            'badge': '🌿 Organic Vitality Booster',
            'action_type': 'Preventative Foliar & Root Microbiome Shield',
            'eco_score': 100,
            'cost_per_acre': '₹220 – ₹300',
            'phi_days': '0 Days',
            'bee_safety': 'Completely pollinator friendly',
            'ingredients': 'Humic substances, Azotobacter, PSB, Seaweed amino acids',
            'dosage': '20 ml Vermiwash or 2 g Bio-consortium per 1 Litre water',
            'schedule': 'Spray every 15 days to maintain natural crop systemic immunity.',
            'soil_benefit': 'Enhances organic carbon and stimulates earthworm root mycorrhizae.'
        },
        'chemical': {
            'title': 'Water-Soluble 19-19-19 Balanced Micronutrient Foliar',
            'badge': '⚗️ Synthetic Growth Enhancer',
            'action_type': 'Direct Foliar Mineral Supplementation',
            'eco_score': 65,
            'cost_per_acre': '₹400 – ₹550',
            'phi_days': '2 Days',
            'bee_safety': 'Low toxicity to pollinators',
            'ingredients': 'Refined Nitrogen, Phosphate, Potash with Chelated Zinc & Iron',
            'dosage': '5 g per 1 Litre water',
            'schedule': 'Apply early morning during active vegetative or flowering flush.',
            'soil_benefit': 'Rapid plant absorption with minimal soil accumulation.'
        }
    }

    if 'healthy' in name_clean:
        return healthy_remedy

    # Exact key match
    if name_clean in remedies:
        return remedies[name_clean]

    # Keyword fuzzy substring matching
    for key, val in remedies.items():
        if key in name_clean:
            return val

    # Substring search by core disease words
    if 'early' in name_clean or 'target' in name_clean:
        return remedies['early_blight']
    if 'late' in name_clean:
        return remedies['late_blight']
    if 'powdery' in name_clean:
        return remedies['powdery_mildew']
    if 'downy' in name_clean:
        return remedies['downy_mildew']
    if 'black' in name_clean or 'spot' in name_clean and 'bacterial' not in name_clean:
        return remedies['black_spot']
    if 'rust' in name_clean:
        return remedies['leaf_rust']
    if 'anthracnose' in name_clean or 'fruit_rot' in name_clean:
        return remedies['anthracnose']
    if 'bacterial' in name_clean:
        return remedies['bacterial_leaf_spot']
    if 'mold' in name_clean or 'mould' in name_clean:
        return remedies['leaf_mold']
    if 'rot' in name_clean or 'wilt' in name_clean or 'root' in name_clean:
        return remedies['root_rot_wilt']
    if 'mosaic' in name_clean or 'virus' in name_clean:
        return remedies['mosaic_virus']

    return healthy_remedy

if __name__ == "__main__":
    test_diseases = ['Powdery Mildew', 'Rose Black Spot', 'Leaf Rust', 'Anthracnose', 'Root Rot Wilt', 'Mosaic Virus']
    for d in test_diseases:
        rem = get_crop_remedies(d)
        print(f"[{d}] -> {rem['disease']} | Organic: {rem['organic']['title']}")
