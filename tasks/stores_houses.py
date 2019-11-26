# task: https://leetcode.com/discuss/interview-question/350248/Google-or-Summer-Intern-OA-2019-or-Stores-and-Houses

# You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional).
# For each house, find the store closest to it.
# Return an integer array result where result[i] should denote the location of the store closest to the i-th house. 
# If many stores are equidistant from a particular house, choose the store with the smallest numerical location. 
# Note that there may be multiple stores and houses at the same location.

# Example 1:

# Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
# Output: [5, 11, 16]
# Explanation: 
# The closest store to the house at location 5 is the store at the same location.
# The closest store to the house at location 10 is the store at the location 11.
# The closest store to the house at location 17 is the store at the location 16.
# Example 2:

# Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
# Output: [2, 3, 2]
# Example 3:

# Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
# Output: [3, 6, 1, 1]

from copy import copy

def closest_store(s, h):
    dist_func = lambda i, j: abs(h[i] - s[j])
    h1 = copy(h)

    s.sort()
    h.sort()
    outputs = {}
    i = 0
    j = 0
    best_j = 0
    min_dist = 100000000
    while i < len(h) and j < len(s):
        dist = dist_func(i, j)
        if dist < min_dist:
            min_dist, best_j = dist, j
        if h[i] <= s[j]:
            outputs[h[i]] = min(outputs.get(h[i], 10000000), s[best_j])
            i += 1
            j += 1
            min_dist = 100000000
            best_j = j
        elif h[i] > s[j]:
            j += 1

    outputs[h[-1]] = min(outputs.get(h[-1], 10000000), s[best_j])
    return [outputs[h1[i]] for i in range(len(h1))]

s = [5, 3, 1, 2, 6]
h = [4, 8, 1, 1]
closest_info = closest_store(s, h)
print(closest_info)