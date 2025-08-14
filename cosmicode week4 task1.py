def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Get user input
input_list = input("Enter a sorted list of numbers (comma-separated): ")
sorted_list = [int(x) for x in input_list.split(',')]
target = int(input("Enter the target value to search for: "))

# Perform search
result = binary_search(sorted_list, target)

# Display result
if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found in the list.")