def gcd(m, n):
    it = 0
    i = min(m, n)
    while i > 0:
        it += 1
        print(f"Iteration {it}: i = {i}")
        if m % i == 0 and n % i == 0:
            break
        i -= 1
    return i, it

result, iterations = gcd(31415, 14142)
time_taken = iterations * 0.001  # 1 millisecond per iteration

print(f"GCD: {result}, Iterations: {iterations}, Time Taken: {time_taken:.3f} seconds")
