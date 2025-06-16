def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Take input from user
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
numbers = list(map(int, user_input.split()))

# Sort using Quick Sort
sorted_numbers = quick_sort(numbers)

# Display result
print("Sorted List:", sorted_numbers)

