def binarySearch(arr, size, find):
    low = 0;
    high = size-1;
    mid = 0

    while low <= high:
        mid = (int(low) + int(high)) / 2
        mid = int(mid)

        if find == arr[mid]:
            return mid
        elif find > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

list = [1, 34, 42, 59, 90, 103, 114, 152, 190, 219, 308]
find = int (input('Search integer: '))
result = binarySearch(list, len(list), find)

if result >= 0:
    print(f'Ditemukan, angka {find} ada didalam index {result}')

else:
    print('Tidak ditemukan')
