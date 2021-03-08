import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import rc
import matplotlib


def bisection(f, a, b, eps=10e-9):
    x = 0
    n = 0
    x_list = []
    f_a = f(a)
    f_b = f(b)
    while b - a > 2 * eps:
        n += 1
        x = (a + b) / 2.0
        x_list.append(x)
        if f(x) * f_a < 0:
            b = x
        elif f(x) * f_b < 0:
            a = x
        else:
            break
    return x, n, x_list


def animate(i):
    """
    Функция animate рисует точку на графике, вычисленную в текущей итерации
    """
    x_i = x_list[i]
    print(x_i)
    f_i = f(x_i)
    ax.plot([x_i, x_i], [0, f_i], 'r:')
    ax.plot(x_i, f_i, 'ro')


def f(x):
    return (x ** 3) * (np.exp(x)) * (np.cos(x))


def check(x1, x2, x3):
    print(f(x1))
    print(f(x2))
    print(f(x3))


if __name__ == '__main__':
    # fig, ax = plt.subplots()
    # x = np.arange(-15, 15, 0.0001)
    # ax.grid()
    # ax.plot(x, f(x), 'r', linewidth=1)
    # plt.show()

    a1 = 7
    b1 = 8
    a2 = 4
    b2 = 5
    a3 = 1
    b3 = 2
    x1, _, _ = bisection(f, a1, b1)
    x2, _, _ = bisection(f, a2, b2)
    x3, _, _ = bisection(f, a3, b3)
    check(x1, x2, x3)

    rc('animation', html='jshtml')

    plt.rcParams['figure.figsize'] = [12, 8]

    a = a1
    b = b1
    _, n, x_list = bisection(f, a, b, 10e-3)

    fig, ax = plt.subplots()

    ax.axhline(y=0, color='k')

    ax.plot([a, a], [0, f(a)], 'r:')
    ax.plot([b, b], [0, f(b)], 'r:')

    x = np.arange(a, b, 0.01)
    plt.grid()
    plt.plot(x, f(x), 'b', linewidth=1)
    plt.show()

    animation.FuncAnimation(fig, animate, frames=n)

    print(x1, x2, x3)
