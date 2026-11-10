def freestream(M0, gamma_cold):

    """Ram pressure and temperature ratios of incoming air
    
    Inputs: 
    - freestream Mach number, M0
    - specific heat ratio of the cold air, gamma_cold
    
    Output:
    - Ram temperature ratio, tau_r
    - Ram pressure ratio, pi_r
    """

    tau_r = 1 + 0.5*(gamma_cold - 1)*M0**2
    pi_r = tau_r**(gamma_cold/(gamma_cold - 1))

    return tau_r, pi_r

def compress(pi, e, gamma):

    """Returns temperature ratio and isentropic efficiency for compressing component (e.g. fan, compressor, booster)

    Inputs:
    - Component pressure ratio, pi
    - Component polytropic efficiency, e
    - Specific heat ratio across component, gamma

    Outputs:
    - Component temperature ratio, tau
    - Component isentropic efficiency, eta
    """

    tau = pi**((gamma - 1)/(gamma*e))

    eta = (pi**((gamma - 1)/gamma) - 1)/(tau - 1)

    return tau, eta