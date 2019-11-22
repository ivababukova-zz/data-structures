# task: https://leetcode.com/discuss/interview-question/334191
from copy import copy

def numb_boquets(seq, K, n):
    k = K - 1
    seq.sort()
    b = 0
    seq1 = copy(seq)
    for i in range(len(seq) - 1):
        if seq[i] + 1 == seq[i+1]:
            k -= 1
        else:
            k = K
        if k == 0:
            b += 1
        if b >= n:
            return b
    return b

def binary_search(flowers, low, high, k, n):
    if low > high:
        return -1
    m = int(low + (high - low)/2)
    middle = flowers[m][0]
    bloomed = [f[1] for f in flowers if f[0] <= middle]
    b = numb_boquets(bloomed, k, n)
    if b == n:
        return flowers[m][0]
    if b < n:
        return binary_search(flowers, m + 1, high, k, n)
    if b > n:
        return binary_search(flowers, low, m - 1, k, n)

def min_day_to_bloom(days, K, n):
    roses = []

    for rose, day in enumerate(days):
        roses.append([day, rose])
    roses.sort()

    return binary_search(roses, 0, len(roses) - 1, K, n)

days = [1, 2, 4, 9, 3, 4, 1]
k = 2
n = 2
day = min_day_to_bloom(days, k, n)
print(day)