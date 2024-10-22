def process_array(arr):
   
    arr.insert(3, 120)
    arr[2] = 99
    arr = list(set(arr))
    arr.sort()
    length = len(arr)
    
    return arr, length
arr = [40, 50, 60, 80, 50, 70]
New_array, total_length = process_array(arr)
print(f"New array: {New_array}")
print(f"Total length of the array: {total_length}")
