# # 9. Write a binary search function. It should take a sorted sequence and the item it is looking for.
# # It should return the index of the item if found. It should return -1 if the item is not found.

array_list = [4, 14, 16, 17, 19, 21, 24, 28, 30, 35, 36, 38, 39, 40, 41, 43]
array_len = len(array_list)


def binary_search(arr, item, start, end):
    mid = round((start+end)/2.0)

    if start > end:
        return -1

    if item == arr[mid]:
        print(f'The number {item} was found in index : {mid}')
    elif item < arr[mid]:
        return binary_search(arr, item, start, mid-1)
    else:
        return binary_search(arr, item, mid+1, end)


print(binary_search(array_list, 8, 0, array_len-1))

