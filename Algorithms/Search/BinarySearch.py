def binarySearch(key, arr, start, last):
    if start <= last:
        mid_index = (start + last) // 2
        if key < arr[mid_index]:
            return binarySearch(key, arr, start, mid_index - 1)
        elif key > arr[mid_index]:
            return binarySearch(key, arr, mid_index + 1, last)
        else:
            return mid_index
    
    return -1 #Not Found

def main():
    arr1 = [7,5,10,6,3,9]
    arr2 = [1,3,6,10,12,15,20]
    key = 10
    print(f'Found {key} at position {linearSearch(key, arr1)}')

    print(f'Found {key} at position {binarySearch(key, arr2, 0, len(arr2) - 1)}')

main()