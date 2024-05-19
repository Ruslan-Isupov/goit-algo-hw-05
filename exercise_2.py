def binary_search(arr, x):
    iter = 0
    low = 0
    high = len(arr) - 1
    mid = 0
    # Змінити назву upper_bound
    upper_bound = arr[-1]
    if upper_bound < x:
        return iter, upper_bound
    
    while low <= high:
        iter+=1    
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1 
       
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
      
        else:
            return iter, arr[mid]
 
    return iter, upper_bound 

# example_array = [1, 2, 2.6, 2.8, 3, 9, 10.5, 10.7, 19.887, 19.888, 20, 21.6]
# x = 10
# result = binary_search(arr, x)
# if result != -1:
#     print(f"Element is present at index {result}")
# else:
#     print("Element is not present in array")
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

print(binary_search(arr, 3.8))  # Виведе: (кількість ітерацій, елемент, що співпадає)
print(binary_search(arr, 3.5))  # Виведе: (кількість ітерацій, верхню межу)
print(binary_search(arr, 4))  # Виведе: (кількість ітерацій, верхню межу)
print(binary_search(arr, 6.0)) # Виведе: (кількість ітерацій, верхню межу)

# (3, 3.8)
# (3, 4.6)
# (3, 5.9)




