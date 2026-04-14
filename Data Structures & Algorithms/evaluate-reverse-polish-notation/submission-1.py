class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isNumber(token)[0]:
                stack.append(self.isNumber(token)[1])
            else:
                operator = token
                num2 = stack.pop()
                num1 = stack.pop()
                num1 = self.completeOperation(num1, num2, operator)
                stack.append(num1)
        return stack.pop()

    def isNumber(self, token: str) -> (bool, int):
        if token.isnumeric(): return (True, int(token))
        elif len(token) > 1 and token[0] == '-':
            return(True, int(token))
        else:
            return(False, 0)

    def completeOperation(self, num1: int, num2:int, operator:str) -> int:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(num1 / num2)