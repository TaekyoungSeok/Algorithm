def insertionSort(array, n):
    if n > 1:
        insertionSort(array, n - 1)

        newitem = array[n - 1]
        insert_index = n - 1

        for j in range(n - 2, -1, -1):
            if newitem < array[j]:
                array[j + 1] = array[j]
                insert_index = j

            else:
                break

        array[insert_index] = newitem

    return array

if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]

    print("정렬 전:", data)
    insertionSort(data, len(data))
    print("정렬 후:", data)