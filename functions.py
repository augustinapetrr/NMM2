'''
23.
Lygtis F
Algoritmas F2
Kraštinės sąlygos I
'''

import math
import constants

i = complex(0, 1)

def u_precise_func(x, t):
    return complex(1, t) * math.cos(math.pi / 2 + math.pi * x)

def u_modulus_pwr(x, t):
    return i * constants.d * (1 + t**2) * complex(1, t) * (math.sin(math.pi * x))**3

def f_func(x, t):
    first = (-1) * i * math.sin(math.pi * x)
    second = (-1) * complex(constants.a**2, 1) * math.pi**2 * complex(1, t) * math.sin(math.pi * x)
    third = i * constants.c * complex(1, t) * math.sin(math.pi * x)
    fourth = u_modulus_pwr(x, t)
    f = first + second + third + fourth
    return f

def fill_u_list(t):
    u = []
    for j in range(0, constants.n + 1):
        u.append(u_precise_func(t, constants.h * j))
    return u

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
    second_a = (u_js_pv - 2 * u_js + u_js_mv) / constants.h**2
    second_b = (u_j_pv - 2 * u_j + u_j_mv) / constants.h**2
    second = (-1) * (constants.a**2 + i) * 0.5 * (second_a + second_b)
    third = i * constants.c * (u_js + u_j) * 0.5
    fourth = i * constants.d * (u_js_kv * u_js + u_j_kv * u_j) * 0.5
    fifth = (f_js + f_j) * 0.5
    residual = abs(first + second + third + fourth + fifth)

    return residual