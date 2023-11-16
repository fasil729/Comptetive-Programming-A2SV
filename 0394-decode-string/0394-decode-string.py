class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        ans = ""
        for char in s:
            if char == "]":
                st = ""
                while stack and stack[-1] != "[":
                    st += stack.pop()[::-1]
                st = st[::-1]
                stack.pop()
                num = ""
                while stack and "0" <= stack[-1] <= "9":
                    num += stack.pop()
                num = num[::-1]  
                stack.append(int(num) * st)
            else:
                stack.append(char)
        for char in stack:
            ans += char
        
        return ans
                
                
                
                
        
        