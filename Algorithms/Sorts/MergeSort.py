def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    left_arr = []
    right_arr = []
    mid = len(arr)//2
    for i in range(len(arr)):
        left_arr.append(arr[i])
    for i in range(mid, len(arr)):
        right_arr.append(arr[i])
    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)
    result = merge(left_arr, right_arr)
    return result

def merge(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    return result

def main():
    arr1 = [1,3,5,8]
    arr2 = [2,6,7]
    print(merge(arr1, arr2))
    arr = [3,5,8,9,1,2,0]
    mergeSort(arr)
    print(arr)


main()