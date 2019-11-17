# task: https://leetcode.com/articles/russian-doll-envelopes/
# You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
# One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Note:
# Rotation is not allowed.

# Example:

# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

from copy import copy

def fits(first, second):
    if first[0] > second[0] and first[1] > second[1]:
        return True
    return False

def max_russian_doll(arr):
    arr.sort(reverse=True)
    print(arr)
    res = search(arr, 0, [])
    print(res)

def search(arr, index, partial):
    if index == len(arr):
        return partial
    partial_without = copy(partial)
    if not partial or fits(arr[index], partial[-1]):
        partial.append(arr[index])
        index += 1
        search(arr, index, partial)
    else:
        index += 1
    search(arr, index, partial_without)
    partial = partial if len(partial) > len(partial_without) else partial_without
    return partial

envelopes = [[5,4],[6,4],[6,7],[2,3]]
max_russian_doll(envelopes)