def naive_search(l, target):
    #searching every element in list until reach target
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    #much faster for bigger ordered list since divides and conquer
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if low > high:
        return -1

    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:
        return binary_search(l, target, midpoint + 1, high)
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint - 1)
