class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        
        
        """
        
        operators = ["/", "+", "-", "*"]
        stack = []
        
        for token in tokens:
            
            if token in operators:
                first = stack.pop()
                second = stack.pop()
                if token == "/":
                    result = int(second / first)
                elif token == "-":
                    result = second - first
                elif token == "+":
                    result = second + first
                else:
                    result = second * first
                stack.append(result)
            else:
                stack.append(int(token))
                
        return stack[0]
        
        
        
        
        
        