# task: https://leetcode.com/discuss/interview-question/356520

def get_min_chairs(S, E):
    arr = [(s, 1) for s in S] + [(e, -1) for e in E]
    arr.sort()
    maxi = 0
    chairs = 0
    for i in range(len(arr)):
        chairs += arr[i][1]
        maxi = max(maxi, chairs)
    return maxi

S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]
chairs = get_min_chairs(S, E)
print(chairs)