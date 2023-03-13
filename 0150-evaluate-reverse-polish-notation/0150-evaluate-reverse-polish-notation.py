class Solution(object):
    from math import trunc
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = ['/', '+', '*','-']
        stack = []
        for operand in tokens:
            if operand in op :
                    value = trunc(eval(stack.pop(-2) + operand + stack.pop(-1)))
                    stack.append(str(value))
                
            else:
                    stack.append(operand)
        return int(stack.pop())