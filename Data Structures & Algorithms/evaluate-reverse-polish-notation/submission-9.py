class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens: 
            if c not in '+-*/': 
                stack.append(int(c)) 
            else:  
                if c == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a + b))
                elif c == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b - a))
                elif c == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a * b))
                elif c == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(float(b) / a))

        return stack[-1]