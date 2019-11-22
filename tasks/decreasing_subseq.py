# Given an int array nums of length n. Split it into strictly decreasing subsequences. Output the min number of subsequences you can get by splitting.

# Example 1:

# Input: [5, 2, 4, 3, 1, 6]
# Output: 3
# Explanation:
# You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
# Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
# But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsuquence of the original array.
# Example 2:

# Input: [2, 9, 12, 13, 4, 7, 6, 5, 10]
# Output: 4
# Explanation: [2], [9, 4], [12, 10], [13, 7, 6, 5]
# Example 3:

# Input: [1, 1, 1]
# Output: 3
# Explanation: Because of the strictly descending order you have to split it into 3 subsequences: [1], [1], [1]


def min_subseq(arr):
    subseq = []
    for n in arr:
        if len(subseq) == 0:
            subseq.append([n])
        else:
            added = False
            for j, n1 in enumerate([subseq[i][-1] for i in range(len(subseq))]):
                if n1 > n:
                    subseq[j].append(n)
                    added = True
                    break
            if not added:
                subseq.append([n])

    print(subseq)
arr = [2, 9, 12, 13, 4, 7, 6, 5, 10]
min_subseq(arr)