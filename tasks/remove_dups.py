# task: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

def remove_dups(nums):
    if len(nums) == 0:
        return 0
    length = 1
    prev = nums[0]
    for i, c in enumerate(nums):
        if c != prev:
            nums[length] = c
            length += 1
        prev = c
    return length

nums = []
print(remove_dups(nums))
