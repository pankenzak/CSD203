def quickSort(arr):
    _quickSort(arr, 0, len(arr)-1)

def _quickSort(arr, start, end):
    if start >= end:
        return
    pivot = arr[end]
    j = start -1
    for i in range(start, end + 1):
        if arr[i] > pivot:
            continue
        else:
            j += 1
            arr[i], arr[j]= arr[j], arr[i]
    _quickSort(arr, start, j-1)
    _quickSort(arr, j+1, end)

def main():
    arr = [3,5,8,9,1,2,0]
    quickSort(arr)
    print(arr)


main()