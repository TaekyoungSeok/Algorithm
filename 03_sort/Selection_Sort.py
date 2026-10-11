def selectionSort(array):
    n = len(array)

    for last in range(n - 1, 0, -1):
        k = 0

        for i in range(1, last + 1):
            if array[i] > array[k]:
                k = i

        tmp = array[k]
        array[k] = array[last]
        array[last] = tmp

    return array

if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]

    print("정렬 전:", data)
    selectionSort(data)
    print("정렬 후:", data)