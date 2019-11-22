# task: https://leetcode.com/discuss/interview-question/394347/

def watering_times(plants, cap1, cap2):
    if not plants:
        return 0
    time = 0
    c1 = cap1
    c2 = cap2
    i = 0
    j = len(plants) - 1
    middle, rem = divmod(len(plants), 2)

    while i < j:
        p1 = plants[i]
        p2 = plants[j]
        if p1 > c1:
            c1 = cap1
        c1 = c1 - p1
        if p2 > c2:
            c2 = cap2
        c2 = c2 - p2
        time += 1
        i += 1
        j -= 1
    
    if rem != 0:
        middle_plant = plants[middle]
        if c1 + c2 < middle_plant:
            c1 = cap1
            c2 = cap2
        if c1 + c2 < middle_plant:
            print("ERRROROR")
            return
        time += 1

    return time

    print(plants, cap1, cap2)


plants = [2, 4, 5, 1, 2]
cap1 = 5
cap2 = 7
t = watering_times(plants, cap1, cap2)
print(t)