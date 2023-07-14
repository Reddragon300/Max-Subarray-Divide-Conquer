# Given an array of integers, find the maximum subarray sum (contiguous) using a divide-and-conquer algorithm.


def max_subarray_sum(arr):
    # Base case: If the array has only one element, return that element
    if len(arr) == 1:
        return arr[0]

    # Divide the array into two halves
    mid = len(arr) // 2
    right_half = arr[mid:]
    left_half = arr[:mid]

    # Recursively find the maximum subarray sum for the left and right halves
    max_sum_left = max_subarray_sum(left_half)
    max_sum_right = max_subarray_sum(right_half)

    # Find the maximum subarray sum that crosses the midpoint
    max_sum_cross = max_crossing_sum(arr, mid)

    # Return the maximum of the three sums
    return max(max_sum_left, max_sum_right, max_sum_cross)


def max_crossing_sum(arr, mid):

    # Calculate the maximum sum on the left side of the midpoint
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid - 1, -1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)

    # Calculate the maximum sum on the right side of the midpoint
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid, len(arr)):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)

    # Return the sum of the left and right sides
    return left_sum + right_sum


# Test case 0:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Expected output: 6

# Test case 1: Array with all positive numbers
arr = [1, 2, 3, 4, 5]
print(max_subarray_sum(arr))  # Expected output: 15

# Test case 2: Array with all negative numbers
arr = [-1, -2, -3, -4, -5]
print(max_subarray_sum(arr))  # Expected output: -1

# Test case 3: Array with both positive and negative numbers
arr = [1, -2, 3, -4, 5]
print(max_subarray_sum(arr))  # Expected output: 5

# Test case 4: Array with only one element
arr = [7]
print(max_subarray_sum(arr))  # Expected output: 7

# Test case 5: Array with all zeros
arr = [0, 0, 0, 0, 0]
print(max_subarray_sum(arr))  # Expected output: 0

# Test case 6: Array with alternating positive and negative numbers
arr = [1, -2, 3, -4, 5, -6, 7]
print(max_subarray_sum(arr))  # Expected output: 7

# Test case 7: Array with a single negative number
arr = [-10]
print(max_subarray_sum(arr))  # Expected output: -10
