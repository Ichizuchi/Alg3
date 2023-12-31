import random as rnd
from statistics import correlation
import matplotlib.pyplot as plt
import numpy as np
import timeit


def find(a, b, len):
    for i in range(len):
        if b == a[i]:
            return i
    return -1


def create_graph(b, c, aur, bur):
    y_values = np.linspace(0, max(c), num=5)
    x_values = np.linspace(0, b[-1], num=11)
    plt.scatter(b, c, s=5)

    y_line = aur * np.array(b) + bur
    plt.plot(b, y_line, color='red')

    plt.title("График")
    plt.xlabel("X-ось")
    plt.ylabel("Y-ось")
    plt.xticks(x_values)
    plt.yticks(y_values)
    correlation_coefficient = np.corrcoef(c, y_line)[0, 1]
    return correlation_coefficient


correlation = []
for iter in [1, 2]:
    x = []
    time = []
    x2 = []
    xtime = []
    randmax = 100000
    for i in range(10, 1001, 10):
        x.append(i)
        a = [rnd.randint(1, randmax) for j in range(i)]
        if iter == 1:
            b = a[rnd.randint(1, len(a)-1)]
        else:
            b = randmax+1
        timer = timeit.timeit(lambda: find(a, b, i), number=1)
        time.append(timer)
        index = find(a, b, i)

        if index != -1:
            print("№", i, "С числом b = ", "Время = ", timer)
        else:
            print("№", i, " Время = ", timer)

    for i, j in zip(x, time):
        x2.append(i**2)
        xtime.append(i*j)
    # Вычисление коэффицентов в системе уравнений метода наименьших квадратов
    sx = sum(x)
    stime = sum(time)
    sx2 = sum(x2)
    sxtime = sum(xtime)
    n = len(x)
  
    k = sx2/sx
    bur = (sxtime - k*stime)/(sx-k*n)
    aur = (stime - bur*n)/sx
    plt.figure(iter)
    # График
    correlation.append(create_graph(x, time, aur, bur))

print("Коэффициент корреляции в первом случае =",
      correlation[0], "\nа во втором случае =", correlation[1])

# Показ графика
plt.show()
