import timeit
import matplotlib.pyplot as plt
import pandas as pd
import math

def F_rec(n):
    if n == 1:
        return 1
    sign = -1 if n % 2 == 1 else 1
    return sign * (math.factorial(n) // F_rec(n - 1) - G_rec(n - 1))

def G_rec(n):
    if n == 1:
        return 1
    return math.factorial(n - 1) + G_rec(n - 1)

def F_G_iter(n):
    F = [0] * (n + 1)
    G = [0] * (n + 1)
    F[1] = G[1] = 1

    fact_n = 1 
    fact_n1 = 1  

    for i in range(2, n + 1):
        fact_n1 = fact_n        
        fact_n *= i             
        sign = -1 if i % 2 == 1 else 1
        G[i] = fact_n1 + G[i - 1]
        F[i] = sign * (fact_n // F[i - 1] - G[i - 1])

    return F[n], G[n]

results = []
for i in range(2, 20):
    try:
        t_rec = timeit.timeit(lambda: F_rec(i), number=1)
    except RecursionError:
        t_rec = None
    t_itr = timeit.timeit(lambda: F_G_iter(i), number=1)
    results.append((i, t_rec, t_itr))

df = pd.DataFrame(results, columns=["n", "Рекурсивное время (сек)", "Итеративное время (сек)"])
print(df)

plt.figure(figsize=(10, 6))
plt.plot(df["n"], df["Рекурсивное время (сек)"], label="Рекурсия", marker='o', color='blue')
plt.plot(df["n"], df["Итеративное время (сек)"], label="Итерация", marker='s', color='green')
plt.xlabel("n")
plt.ylabel("Время (сек)")
plt.title("Сравнение времени: рекурсивный vs итеративный подход")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

