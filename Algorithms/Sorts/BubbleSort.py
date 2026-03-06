def bubbleSort(arr):
    for j in range(len(arr)):
        swapCount = 0
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapCount += 1
            else:
                continue
            
        if swapCount == 0:
            break

def main():
    arr = [3,5,8,9,1,2,0]
    bubbleSort(arr)
    print(arr)


main()
