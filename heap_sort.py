def heapify(arr, heapSize, root):
    largest = root
    leftChild = 2 * root + 1
    rightChild = 2 * root + 2

    if leftChild < heapSize and arr[largest] < arr[leftChild]:
        largest = leftChild

    if rightChild < heapSize and arr[largest] < arr[rightChild]:
        largest = rightChild

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, heapSize, largest)


def heapSort(arr):
    arrLength = len(arr)

    # Build max heap
    for i in range(int(arrLength/2 - 1), -1, -1):
        heapify(arr, arrLength, i)

    # Sort element in ascending order
    for i in range(arrLength - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':

    print('\n========== Test 1: One element ==========')
    arr = [10]
    print('Pre-sort: ', arr)
    heapSort(arr)
    print('Post-sort: ', arr)

    print('\n========== Test 2: Multiple +ve elements ==========')
    arr = [12, 11, 13, 5, 6, 7]
    print('Pre-sort: ', arr)
    heapSort(arr)
    print('Post-sort: ', arr)

    print('\n========== Test 3: Multiple -ve elements ==========')
    arr = [-12, -11, -13, -5, -6, -7]
    print('Pre-sort: ', arr)
    heapSort(arr)
    print('Post-sort: ', arr)

    print('\n========== Test 4: Mix of +ve and -ve elements ==========')
    arr = [12, 20, -8, 4, -2, -20]
    print('Pre-sort: ', arr)
    heapSort(arr)
    print('Post-sort: ', arr)

    print('\n========== Test 5: Ascending order ==========')
    arr = [-100, -80, -5, 0, 2, 5, 200]
    print('Pre-sort: ', arr)
    heapSort(arr)
    print('Post-sort: ', arr)

    print('\n========== Test 6: Descending order ==========')
    arr = [200, 5, 2, 0, -5, -80, -100]
    print('Pre-sort: ', arr)
    heapSort(arr)
    print('Post-sort: ', arr)