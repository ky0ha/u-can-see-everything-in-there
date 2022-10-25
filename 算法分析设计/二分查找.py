def bin_search(array, key):
    left, right = 0, len(array)
    mid = 0
    while left<right:
        mid = (right - left)//2 + left
        if key<array[mid]:
            right = mid - 1
        elif key>array[mid]:
            left = mid + 1
        else:
            return mid
    else:
        if array[left] > key:
            left -= 1
        if array[right] < key:
            right += 1
        return left, right

l = [1, 2, 3, 4, 5, 7, 8, 9]

print(bin_search(l, 6))