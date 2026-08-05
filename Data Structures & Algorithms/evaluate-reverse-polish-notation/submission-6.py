class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            stack.append(i)

        ops = {'+', '-', '*', '/'}

        if stack[-1] not in ops:
            return int(stack.pop())
        
        def rec(stack: []) -> int:
            op = stack.pop()
            op1 = 0
            op2 = 0
            if stack[-1] in ops:
                op1 = rec(stack)
            else:
                op1 = int(stack.pop())
            if stack[-1] in ops:
                op2 = rec(stack)
            else:
                op2 = int(stack.pop())
            
            if op == '+':
                result = op2 + op1
            elif op == '-':
                result = op2 - op1
            elif op == '*':
                result = op2 * op1
            elif op == '/':
                result = int(op2 / op1)

            return result

        return rec(stack)

        