def sort(arr):
    if len(arr) < 2:
        return arr
    p = arr[0]
    lt = []
    gt = []
    for i in arr[1:]:
        if i > p:
            gt.append(i)
        else:
            lt.append(i)
    return sort(lt) + [p] + sort(gt)

