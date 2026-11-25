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

print("lesson 5: lists and tuples")

# Lists are changeable: you can add or update items.
favorite_foods = ["pizza", "pasta", "salad"]
print("Favorite foods:", favorite_foods)

favorite_foods.append("sushi")
favorite_foods[1] = "rice"

print("Updated foods:", favorite_foods)

print("Each food:")
for food in favorite_foods:
    print(food)

# Tuples are ordered, but their items cannot be changed.
coordinates = (10, 20)
x, y = coordinates
print(f"x: {x}, y: {y}")

