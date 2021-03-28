def rectangle(f, a, b, n, height='left'):
    h = float(b - a) / n
    if height == 'left':
        start = a
    elif height == 'mid':
        start = a + h / 2.0
    else:
        start = a + h
    result = 0
    for i in range(n):
        result += f((start) + i * h)
    result *= h
    return result


def test_rectangle_one_exact_result():
    """Compare one hand-computed result."""
    from math import exp
    f = lambda x: 3 * (x**2) * exp(x**3)
    method = ['left', 'mid', 'right']
    n = 2
    exact = [0.4249306699000599, 1.3817914596908085, 4.5023534125886275]
    tol = 1E-14
    for i in range(len(method)):
        numerical = rectangle(f, 0, 1, n, method[i])
        err = abs(exact[i] - numerical)
        success = err < tol
        msg = 'i=%d, err=%g' % (i, err)
        assert success, msg
        print(msg)


def test_rectangle_linear():
    """Check that linear functions are integrated exactly for midpoint
    and correction term for others"""
    method = ['left', 'mid', 'right']
    f = lambda x: 6 * x - 4
    slope = 6
    F = lambda x: 3 * x**2 - 4 * x  # Anti-derivative
    a = 1.2
    b = 4.4
    exact = F(b) - F(a)
    tol = 1E-13 # changed tol
    for n in 2, 20, 21:
        h = float(b - a) / n
        C = n * (0.5 * slope * h**2)    # Correction term
        for i in range(len(method)):
            numerical = rectangle(f, a, b, n, method[i])
            if (method[i] == 'left'):
                numerical += C
            elif (method[i] == 'right'):
                numerical -= C
            err = abs(exact - numerical)
            assert err < tol, 'n = %d, err = %g' % (n, err)


def test_rectangle_conv_rate():
    """Check empirical convergence rates against the expected -2
    for midpoint, and -1 for others."""
    from math import exp
    method = ['left', 'mid', 'right']
    f = lambda x: 3 * (x**2) * exp(x**3)
    F = lambda x: exp(x**3)
    a = 1.1
    b = 1.9
    tol = 0.01
    for i in range(len(method)):
        r = convergence_rates(f, F, a, b, method[i], 14)
        print(method[i])
        print(r)
        if (method[i] == 'left') or (method[i] == 'right'):
            assert abs(abs(r[-1]) - 1) < tol, r[-4:]
        else:
            assert abs(abs(r[-1]) - 2) < tol, r[-4:]


def convergence_rates(f, F, a, b, height, num_experiments=14):
    from math import log
    from numpy import zeros
    exact = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments - 1)
    for i in range(num_experiments):
        n[i] = 2**(i + 1)
        numerical = rectangle(f, a, b, n[i], height)
        E[i] = abs(exact - numerical)
        if i > 0:
            r_im1 = log(E[i] / E[i - 1]) / log(float(n[i]) / n[i - 1])
            r[i - 1] = float('%.2f' % r_im1)
    return r


test_rectangle_one_exact_result()
test_rectangle_linear()
test_rectangle_conv_rate()
