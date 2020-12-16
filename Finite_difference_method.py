import numpy as np

def finite_difference_method(zero_template, eps):
    """
    Finite difference method to solve Dirichlet problem for the Laplace equation
    
    :param zero_tamplate: 2D array
    :param eps: int
    :return: u k
    """

    u, temp = np.copy(zero_template), np.copy(zero_template)
    k = 0

    while (abs(temp) >= eps).any():
        k += 1
        for m in range(1, 5):
            for n in range(1, 5):
                u[m, n] = 0.25 * (zero_template[m-1, n] + zero_template[m+1, n] + zero_template[m, n+1] + zero_template[m, n-1])

        temp = zero_template - u
        zero_template = np.copy(u)

    return u, k

def parabola(u):
    """
    Finite difference method to solve mixed parabolic problem
    
    :param u: 2D array
    :return u: 2D array - solution
    """

    for j in range(len(u)-1):
        for i in range(1, len(u)-1):
            u[j+1, i] = 1 / 6 * (u[j, i+1] + 4 * u[j, i] + u[j, i-1])
    
    return u
    