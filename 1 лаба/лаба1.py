def seq(n):
    return (5 * n ** 3 - 3 * n**2) / (n**3 + 1)
for n in range(1, 10000000 + 1):
    print(n, seq(n))
