# task: https://leetcode.com/problems/k-closest-points-to-origin/
import random

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def kClosest(points, k):
    sort(points, 0, len(points)-1, k)
    return points[:k]

def sort(points, i, j, k):
    if i >= j:
        return
    pivot = random.randint(i, j)
    swap(points, i, pivot)
    mid = partition(points, i, j)
    if k > mid:
        sort(points, mid + 1, j, k - (mid))
    elif k < mid:
        sort(points, i, mid - 1, k)

def partition(arr, i, j):
    pivot = arr[i]
    p = i
    i += 1

    while True:
        while i < j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        swap(arr, i, j)

    swap(arr, p, j)
    return j

K = 2
A = [7, 21, 4, 2, 6, 12, 8, 3, 0, 9, 10]
print(kClosest(A, 7))
# print(quick_select(A, 0, len(A) - 1, 3))
# print(A)