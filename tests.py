import constants
import functions

def print_test1_help(residual_1, residual_2):
    print("Residual ratio: ", residual_1 / residual_2)

def print_test2_help(residual_1, residual_2):
    print("Residual ratio: ", residual_1 / residual_2)

def first_test(x, t):
    print("FIRST TEST")
    residual = functions.test_1(x, t)
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual, "\n")
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_2 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_2)
    print_test1_help(residual, residual_2)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_3 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_3)
    print_test1_help(residual_2, residual_3)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_4 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_4)
    print_test1_help(residual_3, residual_4)
    
    # Restoring values
    constants.h = constants.h * 1000
    constants.tau = constants.tau * 1000
    constants.n = constants.n / 1000

def second_test(x, t):
    print("\n\nSECOND TEST")
    residual = functions.test_2(x, t)
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual, "\n")
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_2 = functions.test_2(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_2)
    print_test2_help(residual, residual_2)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_3 = functions.test_2(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_3)
    print_test2_help(residual_2, residual_3)
    constants.n = constants.n * 10
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_4 = functions.test_2(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_4)
    print_test2_help(residual_3, residual_4)

    # Restoring values
    constants.h = constants.h * 1000
    constants.tau = constants.tau * 1000
    constants.n = constants.n / 1000