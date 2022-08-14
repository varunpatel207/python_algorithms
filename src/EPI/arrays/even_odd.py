def even_odd(arr):
    even = 0
    odd = len(arr) - 1

    while even < odd:
        if arr[even] % 2 == 0:
            even += 1
        else:
            arr[even], arr[odd] = arr[odd], arr[even]
            odd -= 1

        print(arr)

arr = [3, 5, 12, 18, 17, 23, 24]
even_odd(arr)
