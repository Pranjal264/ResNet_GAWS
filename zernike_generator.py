import numpy as np
from scipy.special import factorial

def zernike_gen(n, m, p, dim):
    """
    Generate Zernike polynomial of order (n, m) on a grid of dimensions (dim, dim).

    Parameters:
    - n (int): Radial order of the Zernike polynomial.
    - m (int): Azimuthal order of the Zernike polynomial.
    - p (int): Parameter specifying the type of Zernike polynomial.
              - If p == 0: Zernike polynomial with azimuthal frequency m (m can only be 0).
              - If p == 1: Zernike polynomial with azimuthal frequency m, sin(m*theta).
              - If p == 2: Zernike polynomial with azimuthal frequency m, cos(m*theta).
    - dim (int): The dimension of the output grid.

    Returns:
    numpy.ndarray: Zernike polynomial values on the specified grid.

    Example:
    zernike_gen(3, 1, 1, 64)
    """
    x = np.linspace(-1, 1, dim)
    y = np.linspace(1, -1, dim)
    x, y = np.meshgrid(x, y)

    r = np.sqrt(x**2 + y**2)
    # c = r < 1

    theta = np.arctan2(-y, -x) + np.pi
    sum_ = 0

    for s in np.arange(0, np.floor((n - m) / 2 + 1), 1):
        sum_ = sum_ + ((-1)**s * factorial(n - s) / (factorial(s) *
                                                             factorial((n + m) / 2 - s) *
                                                             factorial((n - m) / 2 - s)) * r**(n - 2 * s))

    r_nm = sum_

    if p == 0:
        z = np.sqrt(n + 1) * r_nm
    elif p == 1:
        z = -1 * np.sqrt(n + 1) * np.sqrt(2) * r_nm * np.sin(m * theta)
    elif p == 2:
        z = np.sqrt(n + 1) * np.sqrt(2) * r_nm * np.cos(m * theta)
    else:
        raise ValueError("Invalid value for parameter 'p'. Use 0, 1, or 2.")

    return z  # * c


def zernikegenerator(od, dim):
    """
    Generate Zernike polynomials up to the given order.

    Parameters:
    - od (int): The maximum order of Zernike polynomials to generate.
    - dim (int): The dimension of the output grid.

    Returns:
    numpy.ndarray: Array containing Zernike polynomials up to the specified order.

    Example:
    zernikegenerator(3, 64)
    """
    n = []
    m = []
    p = []
    x = 0
    while x <= od:
        y = np.arange(0, x + 1, 1)
        for i, y_val in enumerate(y):
            if np.remainder((x - y_val), 2) == 0:
                if y_val == 0:
                    m.append(y_val)
                    n.append(x)
                    p.append(0)
                else:
                    m.append(y_val)
                    n.append(x)
                    p.append(1)
                    m.append(y_val)
                    n.append(x)
                    p.append(2)

        x += 1

    nn = []
    mm = []
    pp = []
    for i, m_val in enumerate(m):
        if m_val == 0:
            nn.append(n[i])
            mm.append(m_val)
            pp.append(0)
        elif i % 2 == 0:
            nn.append(n[i])
            mm.append(m_val)
            pp.append(1)
        else:
            nn.append(n[i])
            mm.append(m_val)
            pp.append(2)

    z = [zernike_gen(nn[i], mm[i], pp[i], dim) for i in range(len(nn))]

    return np.array(z)
