class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operators = {"+","-","/","*"}

        for t in tokens:
            if t not in operators:
                stack.append(int(t))

            else:
                a = stack.pop() #toptop
                
                b = stack.pop() #top

                if t == "+":
                    stack.append(a + b)
                elif t=="-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(a*b)
                elif t == "/":
                    stack.append(int(b/a))
        
        return stack[0]
            