def insertionSort(array):
    n = len(array)

    for i in range(1, n):
        newitem = array[i]
        j = i - 1

        while j >= 0 and newitem < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = newitem

    return array

if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]

    print("정렬 전:", data)
    insertionSort(data)
    print("정렬 후:", data)