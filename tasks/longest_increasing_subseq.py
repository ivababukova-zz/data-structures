# Given an unsorted array of integers, find the length of longest increasing subsequence.
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

# TODO

def longest_subseq(arr):
    arr.sort()
    print(arr)
    get_subseq(arr, 0, [])


def get_subseq(arr, index, partial):
    if not partial or arr[index] > partial[-1]:
        partial.append(arr[index])
    index += 1



arr = [10,9,2,5,3,7,101,18]
longest_subseq(arr)