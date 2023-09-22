class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ind = -1
        for char in s:
            ind += 1
            while ind < len(t) and t[ind] != char:
                ind += 1
        if ind < len(t) and t[ind] == s[-1]:
            return True
        return False