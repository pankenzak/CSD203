def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

def main():
    arr = [3,5,8,9,1,2,0]
    insertionSort(arr)
    print(arr)

main()