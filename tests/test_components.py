from pytest import approx
from src.components import freestream

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