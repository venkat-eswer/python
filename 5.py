print("lesson 6 for python functions")

def flowers():
    print("Roses are red")
    print("Violets are blue")
    print("Sugar is sweet")
    print("And so are you")

print(flowers())

def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(prime_numbers(20))