# task: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = [c for c in s]
        result = "".join(self.traverse(arr))
        print(result)
    
    @staticmethod
    def traverse(arr):
        i = 0
        open_p = []
        while i < len(arr):
            print(arr[i])
            if arr[i] == ")":
                if len(open_p) == 0:
                    arr.pop(i)
                else:
                    open_p.pop()
                    i += 1
            elif arr[i] == "(":
                open_p.append(i)
                i += 1
            else:
                i += 1
        print(arr, open_p)
        if len(open_p) > 0:
            j = 0
            for index in open_p:
                arr.pop(index-j)
                j += 1
        return arr



s = Solution()
s.minRemoveToMakeValid("(a(b(c)d)")