def find_even_index(arr):
    total = 0
    leftsum = 0
    for i in range(len(arr)):
        total += arr[i]
    for i in range(len(arr)):
        total -= arr[i]
        if total == leftsum:
            return i
        leftsum += arr[i]
    return -1