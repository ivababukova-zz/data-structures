from copy import copy

n = 8

def nqueens():
    choices = [i for i in range(1, n+1)]
    res = []
    search(choices, [], res)
    print(len(res))

def diagonals_ok(arr, val):
    j = len(arr)
    for i in range(len(arr)):
        # right diagonal
        if arr[i] + (j - i) == val:
            return False
        # left diagonal
        if arr[i] == val + (j - i):
            return False
    return True

def search(choices, temp, res):
    if len(choices) == 0:
        print(temp)
        res.append(temp)
    for i, val in enumerate(choices):
        if diagonals_ok(temp, val):
            temp1 = copy(temp)
            temp1.append(val)
            search(choices[:i] + choices[i+1:], temp1, res)

nqueens()
