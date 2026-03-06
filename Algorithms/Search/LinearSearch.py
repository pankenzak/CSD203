def linearSearch(key, arr):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
        
def main():
    arr1 = [7,5,10,6,3,9]
    arr2 = [1,3,6,10,12,15,20]
    key = 10
    print(f'Found {key} at position {linearSearch(key, arr1)}')

    print(f'Found {key} at position {binarySearch(key, arr2, 0, len(arr2) - 1)}')

main()