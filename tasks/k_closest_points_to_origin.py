# task: https://leetcode.com/problems/k-closest-points-to-origin/
import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def kClosest(points, k):
    # change dist function if the dimentions of points is different
    dist = lambda i: points[i][0]**2 + points[i][1]**2

    def partial_sort(points, i, j, k):
        if i >= j:
            return
        pivot = random.randint(i, j)
        swap(points, i, pivot)
        mid = partition(points, i, j)
        if k < mid:
            partial_sort(points, i, mid - 1, k)
        elif k > mid:
            partial_sort(points, mid + 1, j, k - mid)

    def partition(arr, i, j):
        pivot = dist(i)
        p = i
        i += 1

        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j:
                break
            swap(arr, i, j)

        swap(arr, p, j)
        return j

    partial_sort(points, 0, len(points) - 1, k)
    return points[:k]


K = 2
A = [7, 21, 4, 2, 6, 12, 8, 3, 0, 9, 10]
points = [[3,3],[5,-1],[-2,4]]
print(kClosest(points, K))
# print(quick_select(A, 0, len(A) - 1, 3))
# print(A)