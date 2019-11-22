
def rotate(m):
    n = len(m[0])

    for i in range(n//2):
        for j in range(i, n - i - 1):
            temp = m[i][j]
            m[i][j] = m[j][n - 1 - i]
            m[j][n - 1 - i] = m[n - 1 - i][n - 1 - j]
            m[n - 1 - i][n - 1 - j] = m[n - 1 - j][i]
            m[n - 1 - j][i] = temp

    for l in m:
        print(l)

m = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for l in m:
    print(l)
print("****")
rotate(m)