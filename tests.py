import constants
import functions


def first_test(x, t):
    print("FIRST TEST")
    residual = functions.test_1(x, t)
    print("Initial values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual)
    constants.h = constants.h / 10
    constants.tau = constants.tau / 10
    residual_2 = functions.test_1(x, t)
    print("Changed values: tau = ", constants.tau, ", h = ", constants.h, "\nResidual = ", residual_2)
    print("\nResidual ratio: ", residual / residual_2)
    if residual / residual_2 >= 0.95 and residual / residual_2 <= 1.05:
        print("First test - OK!\n")
    else:
        print("First test - failed.\n")

    # Restoring values
    constants.h = constants.h * 10
    constants.tau = constants.tau * 10