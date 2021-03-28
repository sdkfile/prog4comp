from trapezoidal import trapezoidal


def test_trapezoidal_one_exact_result():
    """Compare one hand-computed result."""
    f = lambda x: x**0.5
    tol = 1E-14
    exact = [4.82842712474619, 5.050258266979605]
    for n in [2, 3]:
        numerical = trapezoidal(f, 0, 4, n)
        err = abs(exact[n - 2] - numerical)
        success = err < tol
        msg = 'error=%g > tol=%g' % (err, tol)
        assert success, msg
        print(msg)


def test_trapezoidal_linear():
    """Check that linear functions are integrated exactly."""
    f = lambda x: 6 * x - 4
    F = lambda x: 3 * x**2 - 4 * x  # Anti-derivative
    a = 1.2
    b = 4.4
    exact = F(b) - F(a)
    tol = 1E-14
    for n in 2, 20, 21:
        numerical = trapezoidal(f, a, b, n)
        err = abs(exact - numerical)
        success = err < tol
        msg = 'n=%d, err=%g' % (n, err)
        assert success, msg


def convergence_rates(f, F, a, b, num_experiments=14):
    from math import log
    from numpy import zeros
    exact = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments - 1)
    for i in range(num_experiments):
        n[i] = 2**(i + 1)
        numerical = trapezoidal(f, a, b, n[i])
        E[i] = abs(exact - numerical)
        if i > 0:
            r_im1 = log(E[i] / E[i - 1]) / log(float(n[i]) / n[i - 1])
            r[i - 1] = float('%.2f' % r_im1)  # Truncate to two decimals
    return r


def test_trapezoidal_conv_rate():
    """Check empirical convergence rates against the expected -2."""
    f = lambda x: x**0.5
    F = lambda x: (2.0 / 3) * x**(3.0 / 2)
    a = 0.0 + 0.1
    b = 4.0         # a adjusted by 0.1
    r = convergence_rates(f, F, a, b, 14)
    print(r)
    tol = 0.01
    assert abs(abs(r[-1]) - 2) < tol, r[-4:]


test_trapezoidal_one_exact_result()
test_trapezoidal_conv_rate()
