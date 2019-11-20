# task: https://leetcode.com/discuss/interview-question/396769/

def get_max_time(t):
    T = []
    for i, c in enumerate(t):
        if c == "?":
            if i == 0:
                if t[i+1] == "?" or int(t[i+1]) < 3:
                    T.append("2")
                else:
                    T.append("1")
            elif i == 1:
                if T[-1] == "2":
                    T.append("3")
                else:
                    T.append("9") 
            elif i == 3:
                T.append("5")
            elif i == 4:
                T.append("9")
        else:
            T.append(c)
    return "".join(T)

mytime = "?4:5?"
maxi = get_max_time(mytime)
print(maxi)