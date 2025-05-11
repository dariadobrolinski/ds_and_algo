# constant time O(1)
def get_first_element(arr):
    return arr[0] # no matter how big arr is, the function just grabes one item

# linear time O(n)
def find_max(arr):
    max_val = arr[0]
    for item in arr: # one loop through n elements
        if item > max_val:
            max_val = item
    return max_val 

# quadratic time O(n^2)
def print_all_pairs(arr):
    for i in arr: # loop through n elements
        for j in arr: # loop through n elements
            print(i, j)
# two nested loops > n * n = n^2

# cubic time O(n^3)
def count_zero_sums(arr):
    count = 0
    n = len(arr)
    for i in range(n): # loop through n elements
        for j in range(i+1, n): # loop through n elements
            for k in range(j+1, n): # loop through n elements
                if arr[i] + arr[j] + arr[k] == 0:
                    count += 1
    return count
# three loops > n * n * n = n^3

# logarithmic time
def binary_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < key:
            lo = mid + 1
        elif arr[mid] > key:
            hi = mid - 1
        else:
            return mid
    return -1
# each iteration halves the problem