import constants
import functions
from random import random

def print_test_help(residual_1, residual_2):
    print("Residual ratio: ", residual_1 / residual_2)

def first_test(x, t):
    print("FIRST TEST")
    residual = functions.test_1(x, t)
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_2 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_2)
    print_test_help(residual, residual_2)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_3 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_3)
    print_test_help(residual_2, residual_3)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_4 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_4)
    print_test_help(residual_3, residual_4)
    
    constants.h = constants.h * 1000
    constants.tau = constants.tau * 1000
    constants.n = constants.n / 1000

def second_test(x, t):
    print("\n\nSECOND TEST")
    residual = functions.test_2(x, t)
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_2 = functions.test_2(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_2)
    print_test_help(residual, residual_2)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_3 = functions.test_2(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_3)
    print_test_help(residual_2, residual_3)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_4 = functions.test_2(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_4)
    print_test_help(residual_3, residual_4)

    constants.h = constants.h * 1000
    constants.tau = constants.tau * 1000
    constants.n = constants.n / 1000

def third_test():
    print("\n\nTHIRD TEST")
    y = [0j]  # Dėl I kr.są. u_0 = 0
    F_function = [0 for i in range(int(constants.n) + 1)]
    C_function = functions.C_func()

    for i in range(1, int(constants.n)):
        y.append(complex(random(), random()))
    y.append(0j)  # Dėl I kr.są. u_n = 0
    for j in range(1, int(constants.n)):
        F_function[j] = C_function * y[j] - y[j - 1] - y[j + 1]
    y_new = functions.thomas_algorithm(F_function)

    max_delta = functions.max_difference(y_new, y)
    print("Thomas algorithm calculation error:", max_delta)

def global_test(t):
    print('\n\nGLOBAL TEST')
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h)
    max_delta = functions.full_algorithm(t)
    print("Calculation error: ", max_delta)
    constants.n = constants.n * 10
    constants.tau = constants.tau / 10
    constants.h = constants.h / 10
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h)
    max_delta_2 = functions.full_algorithm(t)
    print("Calculation error: ", max_delta_2)
    print("Calculation error ratio: ", max_delta/max_delta_2)
    constants.n = constants.n * 10
    constants.tau = constants.tau / 10
    constants.h = constants.h / 10
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h)
    max_delta_3 = functions.full_algorithm(t)
    print("Calculation error: ", max_delta_3)
    print("Calculation error ratio: ", max_delta_2/max_delta_3)
    constants.n = constants.n * 10
    constants.tau = constants.tau / 10
    constants.h = constants.h / 10
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h)
    max_delta_4 = functions.full_algorithm(t)
    print("Calculation error: ", max_delta_4)
    print("Calculation error ratio: ", max_delta_3/max_delta_4)
    
    constants.h = constants.h * 1000
    constants.tau = constants.tau * 1000
    constants.n = constants.n / 1000