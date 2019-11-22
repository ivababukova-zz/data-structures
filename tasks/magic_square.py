# task: https://leetcode.com/discuss/interview-question/341295/Google-or-Online-Assessment-2019-or-Fill-Matrix

# Given a NxN matrix. Fill the integers from 1 to n*n to this matrix that makes the sum of each row, each column and the two diagonals equal.

# Example 1:

# Input: n = 2
# Output: null
# Explanation: We need to fill [1, 2, 3, 4] into a 2x2 matrix, which is not possible so return null.
# Example 2:

# Input: n = 3
# Output:
# [[8, 3, 4],
#  [1, 5, 9],
#  [6, 7, 2]]
# Explanation: We need to fill [1, 2, 3... 9] into a 3x3 matrix. This is one way to do it
# Each row [8, 3, 4] [1, 5, 9] [6, 7, 2] sum is 15.
# Each column [8, 1, 6] [3, 5, 7] [4, 9, 2] sum is 15.
# The two diagonals [8, 5, 2] [4, 5, 6] sum is 15.
# int[][] fillMatrix(int n) {
# }

from copy import copy


def get_magic_square(n):
    m = [[0 for i in range(n)] for j in range(n)]
    i, _ = divmod(n, 2)
    j = n - 1
    num = 1
    while num <= n*n:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        if m[i][j]:
            j -= 2
            i += 1
            continue
        else:
            m[i][j] = num
            num += 1
        j += 1
        i -= 1

    for l in m:
        print(l)
    


get_magic_square(3)