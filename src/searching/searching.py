# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid = len(arr) // 2
    print(start, end, arr, mid)

    if target == arr[mid]:
        print("found", target, arr[mid])
        return
    elif target < arr[mid]:
        start = 0
        end = arr.index(arr[mid])
        arr = arr[start:end]
        mid = len(arr) // 2
        print(start, end, arr, mid)
        return binary_search(arr, target, start, end)
    elif target > arr[mid]:
        start = arr.index(arr[mid])
        end = len(arr)
        arr = arr[start:end]
        mid = len(arr) // 2
        print(start, end, arr, mid)
        return binary_search(arr, target, start, end)


        # STRETCH: implement an order-agnostic binary search
        # This version of binary search should correctly find
        # the target regardless of whether the input array is
        # sorted in ascending order or in descending order
        # You can implement this function either recursively
        # or iteratively
arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr, 1, 0, len(arr))


# def agnostic_binary_search(arr, target):
# Your code here
