# task: https://leetcode.com/problems/fruit-into-baskets/submissions/

def totalFruit(tree, k):
    i = 0
    counter = {}
    max_fruit = 0
    for j, fruit in enumerate(tree):
        if fruit not in counter or counter[fruit] == 0:
            k -= 1
            counter[fruit] = 1
        else:
            counter[fruit] += 1
        while k < 0:
            counter[tree[i]] -= 1
            if counter[tree[i]] == 0:
                k += 1
            i += 1
            max_fruit = max(max_fruit, j - i + 1)

    max_fruit = max(max_fruit, j - i + 1)
    return max_fruit


t = [3,3,3,1,2,1,1,2,3,3,4]
baskets = 2
print(totalFruit(t, baskets))