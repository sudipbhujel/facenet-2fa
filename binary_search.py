def binary_searches(list, item):
    low = 0
    high = len(list)

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 5, 7, 9]

print(binary_searches(my_list, 9))
print(binary_searches(my_list, -1))

