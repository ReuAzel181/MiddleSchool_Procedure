def gcd_euclidean(m, n):
    it = 0
    iterations = []
    while n:
        it += 1
        iterations.append((m, n))
        m, n = n, m % n
    time_e = it * 0.001  
    return m, iterations, time_e

def gcd_consecutive(m, n):
    it = 0
    iterations = []
    i = min(m, n)
    while i > 0:
        it += 1
        iterations.append((m, n, i))
        if m % i == 0 and n % i == 0:
            break
        i -= 1
    time_c = it * 0.001 
    return i, iterations, time_c

#Euclidean algorithm
result_e, iterations_e, time_e = gcd_euclidean(31415, 14142)

#Consecutive Integer algorithm
result_c, iterations_c, time_c = gcd_consecutive(31415, 14142)

print("\nEuclidean Algorithm:")
print(f"GCD: {result_e}, Iterations: {len(iterations_e)}")
for i, iteration in enumerate(iterations_e, start=1):
    print(f"Iteration {i}: {iteration}")

print("\nConsecutive Integer Algorithm:")
print(f"GCD: {result_c}, Iterations: {len(iterations_c)}")
if len(iterations_c) > 10:
    for i, iteration in enumerate(iterations_c[:10], start=1):
        print(f"Iteration {i}: {iteration}")
    print("& so on...")
else:
    for i, iteration in enumerate(iterations_c, start=1):
        print(f"Iteration {i}: {iteration}")

total_time = time_e + time_c
print(f"\nTotal Time Taken by Euclidean Algorithm: {time_e:.3f} seconds")
print(f"Total Time Taken by CI Algorithm: {time_c:.3f} seconds")
