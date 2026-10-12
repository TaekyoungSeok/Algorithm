def partition(array, p, r):
    pivot = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] < pivot:
            i += 1

            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[i + 1]
    array[i + 1] = array[r]
    array[r] = temp

    return i + 1


def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)

        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)

    return array


if __name__ == "__main__":
    data = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]

    print("정렬 전:", data)
    quickSort(data, 0, len(data) - 1)
    print("정렬 후:", data)