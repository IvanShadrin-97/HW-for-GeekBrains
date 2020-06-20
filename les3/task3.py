def my_func(x: int, y: int, z: int) -> int:
    result = [x, y, z]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(result) - 1):
            if result[i] < result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
            else:
                break
    return sum(result[:1])


print(my_function(1, 2, 3))
