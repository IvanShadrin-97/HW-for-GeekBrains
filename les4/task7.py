def factorial(n):
    result = 1
    last_number = 1
    while last_number <= n:
        yield result
        last_number += 1
        result *= last_number
    return result


for i in enumerate(factorial(4)):
    print(i)
