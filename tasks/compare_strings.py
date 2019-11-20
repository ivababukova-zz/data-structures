# https://leetcode.com/discuss/interview-question/352458/

# C = [3,2]
def compare_strings(a, b):
    a = a.split(",")
    b = b.split(",")
    freq_counter = [0] * 11
    for s in a:
        freq = s.count(min(s))
        freq_counter[freq] += 1
    c = []
    for s in b:
        freq = s.count(min(s))
        c.append(sum(freq_counter[:freq]))
    return c

A = "abcd,aabbbbbc,bd"
B = "aaa,aa"
C = compare_strings(A, B)
print(C)