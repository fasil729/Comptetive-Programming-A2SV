class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []
        def helper(string, o, c):
            if o == n and c == n:
                result.append(string)
                return
            if o > n or c > n:
                return
            helper(string + "(", o + 1, c)
            if o > c:
                helper(string + ")", o, c + 1)
            else:
                return
          
           
        helper("", 0, 0)
        return result
                