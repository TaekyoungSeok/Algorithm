def percolate_down(array, k, n):
    child = 2 * k + 1
    right = 2 * k + 2

    if child < n:
        if right < n and array[child] < array[right]:
            child = right

        if array[k] < array[child]:
            temp = array[k]
            array[k] = array[child]
            array[child] = temp

            percolate_down(array, child, n)


def build_heap(array):
    n = len(array)

    for i in range((n - 2) // 2, -1, -1):
        percolate_down(array, i, n)


def delete_max(array, n):
    max_value = array[0]

    array[0] = array[n - 1]

    percolate_down(array, 0, n - 1)

    return max_value


def heapSort(array):
    build_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[i] = delete_max(array, i + 1)


if __name__ == "__main__":
    data = [4, 2, 8, 7, 3, 3, 5, 1, 9]

    print("정렬 전:", data)
    heapSort(data)
    print("정렬 후:", data)