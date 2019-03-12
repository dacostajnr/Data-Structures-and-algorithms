def fibonacci(number):
    if number<1:
        return 1
    return number*fibonacci(number-1)

print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(0))
print(fibonacci(5))
