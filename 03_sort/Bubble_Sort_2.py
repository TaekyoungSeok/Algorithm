def bubbleSort2(array):
    n = len(array)

    for last in range(n - 1, 0, -1):
        is_sorted = True

        for i in range(last):
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp

                is_sorted = False

        if is_sorted:
            return array

    return array

if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]

    print("정렬 전:", data)
    bubbleSort2(data)
    print("정렬 후:", data)