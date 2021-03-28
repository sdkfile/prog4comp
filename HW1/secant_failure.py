import sys
from newton_failure import f, plot_line


def secant_failure(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0

    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            print('Current x value: ', x1)
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            plot_line(f, x1, f_x1, denominator)
            input('...press enter to continue')
            x = x1 - float(f_x1) / denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
            sys.exit(1)     # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps:
        iteration_counter = -1
    return x, iteration_counter


# x0 = 1.08;   x1 = 1.09
# x0 = 1.09;   x1 = 1.1
# x0 = 1.0;   x1 = 2.3
x0 = 1.0
x1 = 2.4
error_limit = 1e-6

solution, no_iterations = secant_failure(f, x0, x1, eps=1.0e-6)

if no_iterations > 0:    # Solution found
    print("Number of function calls: %d" % (2 + no_iterations))
    print("A solution is: %f" % (solution))
else:
    print("Solution not found!")

"""Error! - denominator zero for x = 360.600893792"""
