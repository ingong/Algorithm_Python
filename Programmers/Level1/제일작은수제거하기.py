def solution(arr):
    arr.remove(min(arr))
    if not arr:
        return [-1]
    return arr


# arr =[4, 3, 2, 1]
# result = solution(arr)
# print(result)
arr1 = [1, 2, 3, 4]
arr1 = [item for item in arr1 if item != 3 and item != 2]
print(arr1)




