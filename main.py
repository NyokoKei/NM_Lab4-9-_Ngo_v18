import numpy as np
from Finite_difference_method import finite_difference_method, parabola

if __name__ == "__main__":
    '''
    zero_template = np.array([[0, 29.389263, 47.552826, 47.552826, 29.389263, 0], 
                            [0, 2.88, 5.76, 8.64, 11.52, 14.4], 
                            [0, 3.84, 7.68, 11.52, 15.36, 19.2], 
                            [0, 3.36, 6.72, 10.08, 13.44, 16.8],
                            [0, 1.92, 3.84, 5.76, 7.68, 9.6], 
                            [0, 0, 0, 0, 0, 0]])
    eps = np.array([0.1, 0.01])
    print(zero_template)
    for i in eps:
        u, k = finite_difference_method(zero_template, i)
        print(k, '\n', u)
    '''
    n = 7
    u = np.zeros([n, n])
    X = np.array([0.1 * i for i in range(n)])
    T = np.array([0.01 * i / 6 for i in range(n)])
    u[0, :] = [np.sin(x + 0.02) for x in X]
    u[:, 0] = [3 * t + 0.02 for t in T]
    u[:, n-1] = 0.581

    print(parabola(u))