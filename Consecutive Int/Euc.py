def gcd(m, n):
    it = 0
    while n:
        it += 1
        print(f"Iteration {it}: m = {m}, n = {n}")
        m, n = n, m % n
    return m, it

result, iterations = gcd(31415, 14142)
time_taken = iterations * 0.001  # 1 millisecond per iteration

print(f"GCD: {result}, Iterations: {iterations}, Time Taken: {time_taken:.3f} seconds")
