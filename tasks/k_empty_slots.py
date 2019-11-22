# task: https://leetcode.com/discuss/interview-question/334191
# Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

# Example:
# Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
# Output: 4
# Explanation:
# day 1: [b, n, n, n, n, n, b]
# The first and the last rose bloom.

# day 2: [b, b, n, n, n, n, b]
# The second rose blooms. Here the first two bloom roses make a bouquet.

# day 3: [b, b, n, n, b, n, b]

# day 4: [b, b, b, n, b, b, b]
# Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.

# int minDaysBloom(int[] roses, int k, int n) {
# }

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