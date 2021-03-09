import math
import matplotlib
import matplotlib.pyplot as plt


def pi(n):
    pi = 0
    for k in range(0, n):
        pi += 1 / ((4 * k + 1) * (4 * k + 3))
    pi *= 8
    return pi


def test(m):
    pi_result = []
    for n in range(1, m):
        pi_result.append(pi(n))
    return pi_result


def absolute(pi_result):
    absolute_result = []
    for i in range(len(pi_result)):
        absolute_result.append(abs(math.pi - pi_result[i]))
    return absolute_result


def relative(absolute_result, pi_result):
    relative_result = []
    for i in range(len(pi_result)):
        relative_result.append(absolute_result[i] / pi_result[i])
    return relative_result


if __name__ == '__main__':
    fig, ax = plt.subplots()
    pi_result = test(100)
    absolute_result = absolute(pi_result)
    relative_result = relative(absolute_result, pi_result)
    ax.plot(pi_result)
    ax.plot(absolute_result)
    ax.plot(relative_result)
    plt.show()
