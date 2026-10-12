def mergeSort(array, p, r):
    if p < r:
        q = (p + r) // 2

        mergeSort(array, p, q)
        mergeSort(array, q + 1, r)

        merge(array, p, q, r)

    return array

def merge(array, p, q, r):
    tmp = [None] * (r - p + 1)

    i = p
    j = q + 1
    t = 0

    while i <= q and j <= r:
        if array[i] <= array[j]:
            tmp[t] = array[i]
            i += 1
            
        else:
            tmp[t] = array[j]
            j += 1

        t += 1

    while i <= q:
        tmp[t] = array[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = array[j]
        j += 1
        t += 1

    i = p
    t = 0

    while i <= r:
        array[i] = tmp[t]
        i += 1
        t += 1

if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]

    print("정렬 전:", data)
    mergeSort(data, 0, len(data) - 1)
    print("정렬 후:", data)