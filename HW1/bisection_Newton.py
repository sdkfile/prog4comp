import sys
from numpy import tanh
from Newtons_method import Newton


def bisection_Newton(f, dfdx, x_L, x_R, eps, s=0.1):
    f_L = f(x_L)
    if f_L * f(x_R) > 0:
        print("Error! Function does not have opposite signs at interval endpoints!")
        sys.exit(1)
    x_M = float(x_L + x_R) / 2.0
    f_M = f(x_M)
    iteration_counter = 1
    interval_Newton = s * (x_R - x_L)    # Limit for swith to Newton
    while (x_R - x_L) > interval_Newton:
        if f_L * f_M > 0:   # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = float(x_L + x_R) / 2
        f_M = f(x_M)
        iteration_counter += 1
    solution, no_iterations = Newton(f, dfdx, x_M, eps)
    return solution, (iteration_counter + no_iterations)


def f(x):
    return tanh(x)


def dfdx(x):
    return 1 - tanh(x)**2


eps = 1e-6
a = -10
b = 15

solution, no_iterations = bisection_Newton(f, dfdx, a, b, eps)
print("A solution x = %f was reached in %d iterations" % (solution, no_iterations))