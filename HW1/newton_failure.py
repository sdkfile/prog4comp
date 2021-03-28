from numpy import tanh, linspace
import matplotlib.pyplot as plt
import sys


def Newton_failure(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            print('Current x value: ', x)
            plot_line(f, x, f_value, dfdx(x))
            input('...press enter to continue')
            x = x - float(f_value) / dfdx(x)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     # Abort with error
        f_value = f(x)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter


def f(x):
    return tanh(x)


def dfdx(x):
    return 1 - tanh(x)**2


def plot_line(f, xn, f_xn, slope):
    # Plot both f(x) and the tangent
    x_f = linspace(-2, 2, 100)
    y_f = f(x_f)
    x_t = linspace(xn - 2, xn + 2, 10)
    y_t = slope * x_t + (f_xn - slope * xn)  # Straight line: ax + b
    plt.figure()
    plt.plot(x_t, y_t, 'r-', x_f, y_f, 'b-')
    plt.grid('on')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()


def application():
    solution, no_iterations = Newton_failure(f, dfdx, x=1.09, eps=0.001)
    if no_iterations > 0:    # Solution found
        print("Number of function calls: %d" % (1 + 2 * no_iterations))
        print("A solution is: %f" % (solution))
    else:
        print("Solution not found!")


if __name__ == '__main__':
    application()

"""Number of function calls: 19
A solution is: nan
is shown when x is set to be 1.09. So Newton's method diverges."""
