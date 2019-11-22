# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum of ‘k’ 
# consecutive elements in the array.

def max_sum(arr, k):
    suma = 0
    i = 0
    for j, el in enumerate(arr):
        if k > 0:
            suma += el
            k -= 1
        else:
            new_suma = suma + el - arr[i]
            suma = max(suma, new_suma)
            i += 1
    return suma

A = [100, 200, 300, 400]
k = 2
s = max_sum(A, k)
print(s)