def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 100]
target = 100
result = binary_search(arr, target)

if result = -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
