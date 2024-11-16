"""
A combination is a mathematical technique that determines the number of possible arrangements
in a collection of items where the order of the selection does not matter.
"""
n = int(input("enter the number to be combined: "))
k = int(input(f"how much time should {n} combination taken at a time? "))

def combination(n,k):
    factorial_n = 1
    factorial_k = 1
    n_minus_k_fact = 1
    for i in range(1,n+1):
        factorial_n = i*factorial_n
    for x in range(1,k+1):
        factorial_k = x*factorial_k
    for y in range(1,n-k+1):
        n_minus_k_fact = y*n_minus_k_fact
    return factorial_n/(factorial_k*n_minus_k_fact)

if k>n:
    print("invalid value.")
    input("click any key to end")
else:
    print(f"The combination of {n} taken {k} at a time is",combination(n,k))
    input("click any key to end")