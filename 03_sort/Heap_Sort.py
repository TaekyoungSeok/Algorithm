def percolateDown(array, k, n):
    child = 2 * k + 1
    right = 2 * k + 2

    if child < n:
        if right < n and array[child] < array[right]:
            child = right

        if array[k] < array[child]:
            temp = array[k]
            array[k] = array[child]
            array[child] = temp

            percolateDown(array, child, n)

def buildHeap(array):
    n = len(array)

    for i in range((n - 2) // 2, -1, -1):
        percolateDown(array, i, n)

def deleteMax(array, n):
    max_value = array[0]

    array[0] = array[n - 1]

    percolateDown(array, 0, n - 1)

    return max_value

def heapSort(array):
    buildHeap(array)

    for i in range(len(array) - 1, 0, -1):
        array[i] = deleteMax(array, i + 1)

if __name__ == "__main__":
    data = [4, 2, 8, 7, 3, 3, 5, 1, 9]

    print("정렬 전:", data)
    heapSort(data)
    print("정렬 후:", data)