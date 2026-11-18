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

def burner(T_t3, T_t4, cp_c, cp_t, eta_b, H_b):

    """Returns fuel to air ratio
    
    Inputs:
    - Burner inlet stagnation temperature, T_t3
    - Burner outlet stagnation temperature, T_t4
    - Cold air specific heat capacity, cp_c
    - Hot exhaust specific heat capacity, cp_t
    - Burner efficiency, eta_b
    - Burner fuel heat of reaction, H_b
    
    Outputs:
    - Fuel to air ratio, f
    """

    f = (cp_c*T_t3 - cp_t*T_t4) / (cp_t * T_t4 - eta_b*H_b)

    return f