from pytest import approx
from src.cycle import cycle

def test_cycle_mattingly():

    """Tests full separate exhaust turbofan against Mattingly Example 7-6.

    Inputs converted to SI. Expected values from pp. 398 to 400,
    final results converted to SI.

    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6.
    """

    inputs = {
        "M0": 0.8,
        "T0": 390 / 1.8,              
        "gamma_c": 1.4,
        "gamma_t": 1.33,
        "cp_c": 0.240 * 4186.8,        
        "cp_t": 0.276 * 4186.8,       
        "H_b": 18400 * 2326,          
        "pi_d": 0.99,
        "pi_b": 0.96,
        "pi_n": 0.99,
        "pi_fn": 0.99,
        "e_c": 0.90,
        "e_f": 0.89,
        "e_t": 0.89,
        "eta_b": 0.99,
        "eta_m": 0.99,
        "P0_over_P9": 0.9,
        "P0_over_P19": 0.9,
        "T_t4": 3000 / 1.8,            
        "pi_c": 36,
        "pi_f": 1.7,
        "alpha": 8,
    }

    r = cycle(inputs)

    assert r["f"] == approx(0.02868, rel=1e-3)
    assert r["tau_t"] == approx(0.54866, rel=1e-3)
    assert r["Pt9_over_P9"] == approx(3.066, rel=1e-3)
    assert r["M9"] == approx(1.394, rel=1e-3)
    assert r["V9_over_a0"] == approx(2.427, rel=1e-3)
    assert r["M19"] == approx(1.154, rel=1e-3)
    assert r["V19_over_a0"] == approx(1.186, rel=1e-3)


    assert r["specific_thrust"] == approx(18.02 * 9.80665, rel=1e-3)    
    assert r["specific_fuel_consumption"] == approx(0.6366 * 0.4535924 / (3600 * 4.448222), rel=1e-3)  