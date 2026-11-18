from pytest import approx
from src.components import *

def test_freestream_mattingly():

    """Tests the freestream function against known inputs and outputs
    
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398
    """

    tau_r, pi_r = freestream(0.8, 1.4)
    assert tau_r == approx(1.128, rel=1e-3)
    assert pi_r == approx(1.5243, rel=1e-3)

def test_freestream_static():

    tau_r, pi_r = freestream(0, 1.4)
    assert tau_r == 1
    assert pi_r == 1

def test_compress_compressor():

    """Tests the compressing function against known compressor inputs and outputs
        
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398
    """

    tau_c, eta_c = compress(36, 0.90, 1.4)

    assert tau_c == approx(3.119, rel=1e-3)
    assert eta_c == approx(0.842, rel=1e-3)

def test_compress_fan():

    """Tests the compressing function against known fan inputs and outputs
            
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398-399
    """

    tau_f, eta_f = compress(1.7, 0.89, 1.4)

    assert tau_f == approx(1.1857, rel=1e-3)
    assert eta_f == approx(0.882, rel=1e-3)

def test_burner_mattingly():

    """Tests the burner function against known inputs and outputs, using any consistent units
                
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398-399
    """

    T_t3 = 390 * 1.128 * 3.119

    f = burner(T_t3 = T_t3, T_t4 = 3000, cp_c = 0.240, cp_t = 0.276, eta_b = 0.99, H_b = 18400)

    assert f == approx(0.02868, rel=1e-3)

def test_expand_mattingly():

    """Tests the expansion function against known inputs and outputs, using any consistent units
                    
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398-399
    """

    pi_t, eta_t = expand(tau = 0.54866, e = 0.89, gamma = 1.33)

    assert pi_t == approx(0.06599, rel=1e-3)
    assert eta_t == approx(0.920, rel=1e-3)

def test_turbine_tau_mattingly():

    """Tests the turbine temperature ratio function against known inputs and outputs, using any consistent units
                        
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398-399
    """

    T_t2 = 390 * 1.128
    T_t3 = T_t2 * 3.119
    T_t13 = T_t2 * 1.1857

    W = 0.240 * ((T_t3 - T_t2) + 8*(T_t13 - T_t2))

    tau_t = turbine_tau(T_t4 = 3000, f = 0.02868, cp_t = 0.276, eta_m = 0.99, W = W)

    assert tau_t == approx(0.54866, rel=1e-3)

def test_nozzle():

    """Tests the nozzle function against known inputs and outputs, using any consistent units
                            
    Source: Mattingly, Elements of Gas Turbine Propulsion, Example 7-6, p. 398-399
    """

    M9, Tt9_over_T9 = nozzle(Pt_over_P = 3.066, gamma = 1.33)
    M19, Tt19_over_T19 = nozzle(Pt_over_P = 2.286, gamma = 1.4)

    assert M9 == approx(1.394, rel=1e-3)
    assert M19 == approx(1.154, rel=1e-3)

    assert (3000 * 0.54866 / 390) / Tt9_over_T9 == approx(3.196, rel=1e-3)
    assert (1.128 * 1.1857) / Tt19_over_T19 == approx(1.0561, rel=1e-3)