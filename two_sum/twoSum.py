arr1 = [1, 3, 5, 6]
target = 8

arr2 = [4, 7, 2, 6]
target = 12

def two_sum(arr, target):

    values = dict()

    for i, elem in enumerate(arr):
        comp = target - elem

        if comp in values:
            return [values[comp], i]

        values[elem] = i

    return[]

    