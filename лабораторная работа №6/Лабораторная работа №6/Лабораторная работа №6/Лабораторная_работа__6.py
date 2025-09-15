import math
import timeit
import matplotlib.pyplot as plt

def sign(n):
    return 1 if n % 2 == 0 else -1

def F_recursive(n):
    if n < 2:
        return 1
    return sign(n) * (F_recursive(n - 1) / math.factorial(2 * n)  - math.cos(F_recursive(n - 2) + 2))

def F_iterative(n):
    if n < 2:
        return 1
    f2, f1 = 1, 1
    fact = 2
    for i in range(2, n + 1):
        fact *= (2*i - 1) * (2*i)
        cur = sign(i) * (f1 / fact - math.cos(f2 + 2))
        f2, f1 = f1, cur
    return f1

def main():
    start_n = 1
    end_n = 19
    results = []
    for n in range(start_n, end_n + 1):
        tr = timeit.timeit(lambda: F_recursive(n), number=10)
        ti = timeit.timeit(lambda: F_iterative(n), number=10)
        results.append((n, tr, ti))

    print(f"{' n':>4} | {'Рекурсивное время (сек)':>12} | {'Итеративное время (сек)':>12}")
    print("-" * 42)
    for n, tr, ti in results:
        print(f"{n:4d} | {tr:12.6f} | {ti:12.6f}")

    xs = [r[0] for r in results]
    yr = [r[1] for r in results]
    yi = [r[2] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(xs, yr, '--o', label='Рекурсивный')
    plt.plot(xs, yi,  '-o', label='Итеративный')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение времени вычисления F(n)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()


