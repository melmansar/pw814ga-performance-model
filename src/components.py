def freestream(M0, gamma_cold):

    """Recovery pressure and temperature ratios of incoming air
    
    Inputs: 
    - freestream Mach number, M0
    - specific heat ratio of the cold air, gamma_cold
    
    Output:
    - Recovery temperature ratio, tau_r
    - Recovery pressure ratio, pi_r
    """

    tau_r = 1 + 0.5*(gamma_cold - 1)*M0**2
    pi_r = tau_r**(gamma_cold/(gamma_cold - 1))

    return tau_r, pi_r