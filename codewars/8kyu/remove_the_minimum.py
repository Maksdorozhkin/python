# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

def remove_smallest(numbers):
    if not numbers:
        return []
    min_index = min(range(len(numbers)), key=numbers.__getitem__)
    return [num for idx, num in enumerate(numbers) if idx != min_index]


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))


def remove_smallest1(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


print(remove_smallest1([1, 2, 3, 4, 5]))
print(remove_smallest1([5, 3, 2, 1, 4]))
print(remove_smallest1([2, 2, 1, 2, 1]))
