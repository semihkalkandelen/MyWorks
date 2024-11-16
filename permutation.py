"""
Permutation is each of several possible ways in which a set or number of things can be ordered or arranged.
"""
n = int(input("Input the number to calculate its permutation: "))
k = int(input(f"How many elements should be selected for the permutation of{n}? "))

def permutation(n,k):
    factorial_n = 1
    factorial_k = 1
    n_minus_k_fact = 1
    for i in range(1,n+1):
        factorial_n = i*factorial_n
    for y in range(1,n-k+1):
        n_minus_k_fact = y*n_minus_k_fact
    return factorial_n/(factorial_k*n_minus_k_fact)

if k>n:
    print("invalid value.")
    input("click any key to end")
else:
    print(f"The combination of {n} taken {k} at a time is",permutation(n,k))
    input("click any key to end")