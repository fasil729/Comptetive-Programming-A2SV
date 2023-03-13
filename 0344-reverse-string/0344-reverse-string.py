class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, start, end):
            if end - start <= 0:
                pass
            else:
                s[start], s[end] = s[end], s[start]
                helper(s, start + 1, end - 1)
        helper(s, 0, len(s) - 1)
        