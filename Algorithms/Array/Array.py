def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

def remove_odds(array):
    result = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result.append(array[i])
    return result;

def reverse_array(array):
    i = 0
    j = len(array) - 1
    while i<j:
        array[i], array[j] = array[j], array[i]
#         tmp = array[i]
#         array[i] = array[j]
#         array[j] = tmp
        i += 1
        j -= 1

def move_zeros(array):
    result = []
    zero_count = 0
    
    for i in range(len(array)):
        if array[i] == 0:
            zero_count += 1
        else:
            result.append(array[i])
    
    for i in range(zero_count):
        result.append(0)
    return result

def find_max(array):
    max_value = array[0]
    for i in range (1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
    return max_value

def find_second_max(array):
    if len(array)<2:
        print("there is no second max number")
        return
    max_value = float("-inf")
    second = float("-inf")
    for i in range(len(array)):
        if array[i] > max_value:
            second = max_value
            max_value = array[i]
        elif array[i] != max_value and array[i] > second:
            second = array[i]
    if second == float("-inf"):
        print("there is no second max number")
        return
            
    return second

if __name__ == "__main__":
    arr = [0, 9, 2, 4, 0, 1, 10, 6, 7, 10]
    print_array(arr)
    print(arr)
#     for index, value in enumerate(arr):
#         print(index, value)
    print(remove_odds(arr))
#     reverse_array(arr)
#     print(arr)
    print(move_zeros(arr))
    print(find_max(arr))
    print(find_second_max(arr))
    
