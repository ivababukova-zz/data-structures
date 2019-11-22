# task: https://leetcode.com/discuss/interview-question/356477


def type_key(keys_positions, i, key, t):
    new_i = keys_positions[key]
    t += abs(i - new_i)
    return new_i, t

def time_to_type_str(keyboard, text):
    keys_positions = {}
    for i, k in enumerate(keyboard):
        keys_positions[k] = i
    i = 0
    t = 0
    for k in text:
        i, t = type_key(keys_positions, i, k, t)
    return t

keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba"
t = time_to_type_str(keyboard, text)
print(t)