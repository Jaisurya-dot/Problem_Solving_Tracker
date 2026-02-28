def binary(arr, high, low, x):
      
    if low > high:
        return [False]      
    mid = (low + high) // 2  
    if arr[mid] == x:
        return [True , mid]
    elif arr[mid] > x:  
        return binary(arr, mid - 1, low, x)
    else:   
        return binary(arr, high, mid + 1, x)
 
 
 
 
matrix  = [[2,4,5],
           [12,45,56],
           [21,32,43]
           ]

 
for i in range(len(matrix)): 
    value = binary(matrix[i], len(matrix[i]) - 1, 0, 4)
    if value[0]:
        print(f'{i} {value[1]}')
        

 