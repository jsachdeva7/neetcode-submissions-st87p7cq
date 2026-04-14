class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # keep two in the stack at a time
        for token in tokens:
            if self.isValidNumber(token):
                stack.append(int(token))
            else:
                operator = token
                num2 = stack.pop() # new number
                num1 = stack.pop() # current expression value
                stack.append(self.performOperation(num1, num2, operator))
        return stack.pop()
    
    def performOperation(self, num1: int, num2: int, operator: str) -> int:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(num1 / num2)

    def isValidNumber(self, string: str) -> bool:
        if (not string[0].isnumeric()) and len(string) == 1:
            return False
        return True
        