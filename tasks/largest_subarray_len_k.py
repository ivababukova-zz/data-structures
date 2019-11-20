# task: https://leetcode.com/discuss/interview-question/352459/

def largest_subarr(A, k):
    maxi = []
    maxi_sum = 0
    for start in range(len(A) - k + 1):
        end = start + k
        suma = sum(A[start:end])
        if suma > maxi_sum:
            maxi = A[start:end]
            maxi_sum = suma
    return maxi


A = [1, 4, 3, 2, 5]
M = largest_subarr(A, 4)
print(M)