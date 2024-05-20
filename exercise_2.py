def binary_search(arr, x):
    iter = 0
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    
    
    while low <= high:
        iter+=1    
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1 
       
        elif arr[mid] > x:   
            high = mid - 1
      
        else:
            return iter, arr[mid]
    
    if low < len(arr):
        return iter, arr[low]
    else:
        return iter, upper_bound
        
 
    



arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

print(binary_search(arr, 3.8))  
print(binary_search(arr, 3.5))  
print(binary_search(arr, 4))  
print(binary_search(arr, 6.0))







