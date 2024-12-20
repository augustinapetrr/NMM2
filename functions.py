'''
23.
Lygtis F
Algoritmas F2
Kraštinės sąlygos I
'''

import math
import constants

i = complex(0, 1)

# T1

def u_precise_func(x, t):
    return complex(1, t) * math.cos(math.pi / 2 + math.pi * x)

def u_modulus_pwr(x, t):
    return (1 + t**2) * (math.sin(math.pi * x))**2

def f_func(x, t):
    first = (-1) * i * math.sin(math.pi * x)
    second = (-1) * complex(constants.a**2, 1) * math.pi**2 * complex(1, t) * math.sin(math.pi * x)
    third = i * constants.c * complex(1, t) * math.sin(math.pi * x)
    fourth = (-1) * i * constants.d * u_modulus_pwr(x, t) * u_precise_func(x, t)
    f = first + second + third + fourth
    return f

def test_1(x, t):
    u_j = u_precise_func(x, t)
    u_j_pv = u_precise_func(x + constants.h, t)
    u_j_mv = u_precise_func(x - constants.h, t)
    u_j_kv = u_modulus_pwr(x, t)
    u_js = u_precise_func(x, t + constants.tau)
    u_js_pv = u_precise_func(x + constants.h, t + constants.tau)
    u_js_mv = u_precise_func(x - constants.h, t + constants.tau)
    u_js_kv = u_modulus_pwr(x, t + constants.tau)
    f_j = f_func(x, t)
    f_js = f_func(x, t + constants.tau)

    first = (u_js - u_j) / constants.tau
    second_a = (u_js_pv - (2 * u_js) + u_js_mv) / constants.h**2
    second_b = (u_j_pv - (2 * u_j) + u_j_mv) / constants.h**2
    second = (-1) * complex(constants.a**2, 1) * 0.5 * (second_a + second_b)
    third = (-1) * i * constants.c * (u_js + u_j) * 0.5
    fourth = (-1) * i * constants.d * (u_js_kv * u_js + u_j_kv * u_j) * 0.5
    fifth = (-1) * (f_js + f_j) * 0.5

    residual = abs(first + second + third + fourth + fifth)
    return residual

# T2

def C_func():
    return 2 + (2 * constants.h**2 / (complex(constants.a**2, 1) * constants.tau))

def F_func(f_j, f_js, u_j, u_js, u_j_kv, u_js_kv, u_j_pv, u_j_mv):
    first = u_j_pv - 2 * u_j + u_j_mv
    h_a = constants.h**2 / complex(constants.a**2, 1)
    second = 2 / constants.tau * u_j
    third = complex(0, constants.c) * (u_js + u_j)
    fourth = complex(0, constants.d) * (u_js_kv * u_js + u_j_kv * u_j)
    fifth = f_j + f_js
    return first + h_a * (second + third + fourth + fifth)

def test_2(x, t):
    u_j = u_precise_func(x, t)
    u_j_pv = u_precise_func(x + constants.h, t)
    u_j_mv = u_precise_func(x - constants.h, t)
    u_j_kv = u_modulus_pwr(x, t)
    u_js = u_precise_func(x, t + constants.tau)
    u_js_pv = u_precise_func(x + constants.h, t + constants.tau)
    u_js_mv = u_precise_func(x - constants.h, t + constants.tau)
    u_js_kv = u_modulus_pwr(x, t + constants.tau)
    f_j = f_func(x, t)
    f_js = f_func(x, t + constants.tau)

    C_function = C_func()
    F_function = F_func(f_j, f_js, u_j, u_js, u_j_kv, u_js_kv, u_j_pv, u_j_mv)
    return abs(u_js_pv - (C_function * u_js) + u_js_mv + F_function)

# T3

def alpha_array():
    C_function = C_func()
    a_array = [0, 0] # alpha_0 neegzistuoja; dėl I kr.są. alpha_1 = 0 
    for i in range(2, int(constants.n)):
        a_array.append(1 / (C_function - a_array[i - 1]))
    a_array.append(0)  # Alpha_N = 0 del I K.S
    return a_array

def max_difference(u_new, u_old):
    max_diff = 0
    for i in range(0, len(u_new)):
        difference = abs(u_old[i] - u_new[i])
        if max_diff < difference:
            max_diff = difference
    return max_diff

def thomas_algorithm(F_function):
    a_array = alpha_array()
    C_function = C_func()
    beta_array = [0, 0]  # beta_0 - neegzistuoja; dėl I kr.są. beta_1 = 0
    u_new = [complex(0, 0) for i in range(int(constants.n) + 1)]

    for i in range(2, int(constants.n) + 1):
        top = F_function[i - 1] + beta_array[i - 1]
        bottom = C_function - a_array[i - 1]
        beta_array.append(top / bottom)

    for k in reversed(range(1, int(constants.n))):
        u_new[k] = (a_array[k + 1] * u_new[k + 1]) + beta_array[k + 1]
    return u_new

# T4

def fill_u_list(t):
    u = []
    for j in range(0, int(constants.n) + 1):
        u.append(u_precise_func(constants.h * j, t))
    return u

def F_function_list(t_current, u, u_js):
    F_function_array = [0j]
    for i in range(1, int(constants.n)):
        u_js_abs_sqr = u_js[i].real**2 + u_js[i].imag**2
        u_abs = u[i].real**2 + u[i].imag**2
        f_j = f_func(constants.h * i, t_current)
        f_js = f_func(constants.h * i, t_current + constants.tau)
        F_function_array.append(F_func(f_j, f_js, u[i], u_js[i], u_abs, u_js_abs_sqr, u[i + 1], u[i - 1]))
    return F_function_array

def u_new_function(u_js, F_function):
    u_new = []
    cont = True
    while cont:
        u_new = thomas_algorithm(F_function)
        max_diff = max_difference(u_new, u_js)
        if max_diff < constants.delta:
            cont = False
        else:
            u_js = list(u_new)
    return u_new


def full_algorithm(t_total):
    t = 0
    u = fill_u_list(t)
    max_difference_array = []
    u_js = list(u)

    while t < t_total:
        F_function = F_function_list(t, u, u_js)
        u_new = u_new_function(u_js, F_function)
        t = t + constants.tau
        u = fill_u_list(t)
        max_difference_array.append(max_difference(u_new, u))
        u_js = list(u_new)

    return max(max_difference_array)