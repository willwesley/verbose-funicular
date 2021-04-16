def sort(arr):
    if len(arr) < 2:
        return arr
    if arr[0] > arr[1]:
        return [arr[1], arr[0]] + arr[2:]
    return arr