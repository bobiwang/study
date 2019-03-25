def factorial(n):
    if n == 0 or n == 1:
        return 1

    product = 1
    while n > 0:
        product = n * product
        n = n - 1
    return product


print(factorial(4))
print(factorial(5))
print(factorial(0))
print(factorial(1))
