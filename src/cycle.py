from src.components import *

def cycle(inputs):

    T0 = inputs["T0"]
    M0 = inputs["M0"]
    gamma_c = inputs["gamma_c"]
    gamma_t = inputs["gamma_t"]
    cp_c = inputs["cp_c"]
    cp_t = inputs["cp_t"]
    alpha = inputs['alpha']
    pi_c = inputs["pi_c"]
    pi_f = inputs["pi_f"]
    pi_d = inputs["pi_d"]
    e_c = inputs["e_c"]
    e_f = inputs["e_f"]
    T_t4 = inputs["T_t4"]
    eta_b = inputs["eta_b"]
    H_b = inputs["H_b"]
    eta_m = inputs["eta_m"]
    e_t = inputs["e_t"]
    pi_b = inputs["pi_b"]
    pi_n = inputs["pi_n"]
    pi_fn = inputs["pi_fn"]
    P0_over_P9 = inputs["P0_over_P9"]
    P0_over_P19 = inputs["P0_over_P19"]

    R_c = (gamma_c - 1)/gamma_c*cp_c
    R_t = (gamma_t - 1)/gamma_t*cp_t

    a0 = (gamma_c*R_c * T0)**0.5
    V0 = a0 * M0

    tau_r, pi_r = freestream(M0, gamma_c)

    T_t2 = T0 * tau_r

    tau_c, eta_c = compress(pi_c, e_c, gamma_c)
    tau_f, eta_f = compress(pi_f, e_f, gamma_c)

    T_t13 = T_t2 * tau_f
    T_t3 = T_t2 * tau_c

    f = burner(T_t3, T_t4, cp_c, cp_t, eta_b, H_b)

    turbine_work = cp_c * ((T_t3 - T_t2) + alpha * (T_t13 - T_t2))

    tau_t = turbine_tau(T_t4, f, cp_t, eta_m, turbine_work)

    pi_t, eta_t = expand(tau_t, e_t, gamma_t)

    T_t5 = T_t4 * tau_t

    Pt9_over_P9 = P0_over_P9 * pi_r * pi_d * pi_c * pi_b * pi_t * pi_n
    Pt19_over_P19 = P0_over_P19 * pi_r * pi_d * pi_f * pi_fn

    M9, Tt9_over_T9 = nozzle(Pt9_over_P9, gamma_t)
    M19, Tt19_over_T19 = nozzle(Pt19_over_P19, gamma_c)

    T9 = T_t5 / Tt9_over_T9
    V9 = M9 *(gamma_t * R_t * T9)**0.5

    T19 = T_t13 / Tt19_over_T19
    V19 = M19 *(gamma_c * R_c * T19)**0.5

    specific_thrust = 1/(1+alpha) * ((1+f)*V9 - V0 + (1+f)*R_t*T9*(1 - P0_over_P9)/V9) + alpha/(1+alpha)*(V19 - V0 +R_c*T19*(1-P0_over_P19)/V19)

    specific_fuel_consumption = f / ((1 + alpha) * specific_thrust)

    results = {
    # freestream and inlet
    "tau_r": tau_r,          
    "pi_r": pi_r,            
    # fan and compressor
    "tau_f": tau_f,          
    "eta_f": eta_f,          
    "tau_c": tau_c,          
    "eta_c": eta_c,          
    # burner
    "f": f,                 
    # turbine
    "tau_t": tau_t,        
    "pi_t": pi_t,          
    "eta_t": eta_t,
    "T_t5": T_t5,      
    # core nozzle
    "Pt9_over_P9": Pt9_over_P9,    
    "M9": M9,                      
    "T9_over_T0": T9 / T0,        
    "V9_over_a0": V9 / a0,        
    # fan nozzle
    "Pt19_over_P19": Pt19_over_P19,  
    "M19": M19,                    
    "T19_over_T0": T19 / T0,       
    "V19_over_a0": V19 / a0,         
    # final
    "specific_thrust": specific_thrust,  
    "specific_fuel_consumption": specific_fuel_consumption,              
    }

    return results