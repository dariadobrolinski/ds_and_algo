# linear search 
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
# checks every element in a list one by one
# time complexity is either O(n) or O(1). O(1) is the best case

# binary search
def binary_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
# works only on sorted lists, repeatedly divides the list in half
# time complexity is always O(log n)

