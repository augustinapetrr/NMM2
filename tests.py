import constants
import functions

def first_test_help(residual_1, residual_2):
    print("Residual ratio: ", residual_1 / residual_2)
    if residual_1 / residual_2 >= 95 and residual_1 / residual_2 <= 105:
        print("Residual ratio - OK!\n")
    else:
        print("Residual ratio - failed.\n")


def first_test(x, t):
    print("FIRST TEST")
    residual = functions.test_1(x, t)
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual, "\n")
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_2 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_2)
    first_test_help(residual, residual_2)
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_3 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_3)
    first_test_help(residual_2, residual_3)
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_4 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_4)
    first_test_help(residual_3, residual_4)
    
    # Restoring values
    constants.h = constants.h * 1000
    constants.tau = constants.tau * 1000