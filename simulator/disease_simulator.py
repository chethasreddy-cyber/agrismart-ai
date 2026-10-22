import math

def simulate_disease_impact(disease_name, current_severity, current_yield, selected_scenario="Treat Now", days=7):
    """
    Simulates disease severity progression and future estimated crop yield impact.
    
    IMPORTANT: This is a simulation/estimation module based on agricultural project rules.
    
    Scenarios:
      1. Treat Now    -> Disease severity decreases sharply; minimal yield loss.
      2. Wait 7 Days  -> Disease progresses for 7 days before control; moderate yield loss.
      3. No Treatment -> Uncontrolled disease spread; severe yield loss.
    """
    # Healthy crop edge-case
    if disease_name.lower() == 'healthy' or current_severity == 0:
        return {
            'selected_scenario': selected_scenario,
            'current_severity': 0.0,
            'future_severity': 0.0,
            'current_yield': round(float(current_yield), 2),
            'future_yield': round(float(current_yield), 2),
            'yield_diff': 0.0,
            'comparison': [
                {'scenario': 'Treat Now', 'future_severity': 0.0, 'future_yield': round(float(current_yield), 2), 'yield_diff': 0.0},
                {'scenario': 'Wait 7 Days', 'future_severity': 0.0, 'future_yield': round(float(current_yield), 2), 'yield_diff': 0.0},
                {'scenario': 'No Treatment', 'future_severity': 0.0, 'future_yield': round(float(current_yield), 2), 'yield_diff': 0.0},
            ]
        }

    scenarios_data = {}

    # 1. Treat Now Simulation
    # Severity drops by ~60% of current value; max yield loss capped at 5%
    sev_treat = max(5.0, current_severity * 0.40)
    loss_factor_treat = (sev_treat / 100.0) * 0.15
    yield_treat = max(0.1, current_yield * (1.0 - loss_factor_treat))
    scenarios_data['Treat Now'] = {
        'future_severity': round(float(sev_treat), 1),
        'future_yield': round(float(yield_treat), 2),
        'yield_diff': round(float(yield_treat - current_yield), 2)
    }

    # 2. Wait 7 Days Simulation
    # Severity increases by +20% over 7 days, then treatment slows it
    sev_wait = min(100.0, current_severity + (days * 2.5))
    loss_factor_wait = (sev_wait / 100.0) * 0.35
    yield_wait = max(0.1, current_yield * (1.0 - loss_factor_wait))
    scenarios_data['Wait 7 Days'] = {
        'future_severity': round(float(sev_wait), 1),
        'future_yield': round(float(yield_wait), 2),
        'yield_diff': round(float(yield_wait - current_yield), 2)
    }

    # 3. No Treatment Simulation
    # Aggressive spread: +35% to +50% severity increase, severe yield drop
    sev_notreat = min(100.0, current_severity + (days * 5.0))
    loss_factor_notreat = (sev_notreat / 100.0) * 0.65
    yield_notreat = max(0.1, current_yield * (1.0 - loss_factor_notreat))
    scenarios_data['No Treatment'] = {
        'future_severity': round(float(sev_notreat), 1),
        'future_yield': round(float(yield_notreat), 2),
        'yield_diff': round(float(yield_notreat - current_yield), 2)
    }

    selected_res = scenarios_data.get(selected_scenario, scenarios_data['Treat Now'])

    comparison_list = []
    for sc_name, sc_vals in scenarios_data.items():
        comparison_list.append({
            'scenario': sc_name,
            'future_severity': sc_vals['future_severity'],
            'future_yield': sc_vals['future_yield'],
            'yield_diff': sc_vals['yield_diff']
        })

    return {
        'disease': disease_name,
        'selected_scenario': selected_scenario,
        'current_severity': round(float(current_severity), 1),
        'future_severity': selected_res['future_severity'],
        'current_yield': round(float(current_yield), 2),
        'future_yield': selected_res['future_yield'],
        'yield_diff': selected_res['yield_diff'],
        'comparison': comparison_list
    }

if __name__ == "__main__":
    res = simulate_disease_impact(
        disease_name="Early Blight",
        current_severity=38.0,
        current_yield=4.20,
        selected_scenario="Treat Now"
    )
    print("=" * 60)
    print("WHAT-IF & DISEASE IMPACT SIMULATOR TEST")
    print("=" * 60)
    print(f"Disease           : {res['disease']}")
    print(f"Current Severity  : {res['current_severity']}%")
    print(f"Current Yield     : {res['current_yield']} tons/acre")
    print(f"Selected Scenario : {res['selected_scenario']}")
    print(f"Future Severity   : {res['future_severity']}% (Simulated)")
    print(f"Future Yield      : {res['future_yield']} tons/acre (Estimated)")
    print(f"Yield Difference  : {res['yield_diff']} tons/acre")
    print("\n--- ALL SCENARIOS COMPARISON TABLE ---")
    print(f"{'Scenario':<15} | {'Future Severity':<16} | {'Future Yield':<20} | {'Diff'}")
    print("-" * 60)
    for item in res['comparison']:
        print(f"{item['scenario']:<15} | {item['future_severity']:>14}% | {item['future_yield']:>15} tons/acre | {item['yield_diff']:>5}")
    print("=" * 60)
