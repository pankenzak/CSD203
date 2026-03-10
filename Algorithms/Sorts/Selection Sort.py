def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

def main():
    arr = [3,5,8,9,1,2,0]
    selectionSort(arr)
    print(arr)


main()