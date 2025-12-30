def quick_sort(arr):
    if len(arr) <=3:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


arr=[9,8,7,4,5,6,3,2-5]
arr=quick_sort(arr)

print(arr)

