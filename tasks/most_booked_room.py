# task: https://leetcode.com/discuss/interview-question/421787/

def get_times_booked(n):
    a, rem = divmod(n, 2)
    return a + rem

def get_most_booked(b):
    bookings = {}
    for item in b:
        item = item.strip("+-")
        if item not in bookings:
            bookings[item] = 0
        bookings[item] += 1
    max_booked = 0
    max_name = ""
    for k in bookings.keys():
        times_booked = get_times_booked(bookings[k])
        if times_booked > max_booked:
            max_booked = times_booked
            max_name = k
    return max_name


b = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
thebest = get_most_booked(b)
print(thebest)