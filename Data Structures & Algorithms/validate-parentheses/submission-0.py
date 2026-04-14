class Solution:
    def __init__(self):
        self.pairs = {'(': ')', '{': '}', '[': ']'}

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        # stack: last in first out (lifo)

        stack = []

        for c in s:
            if self.isOpener(c):
                stack.append(c)
            elif len(stack) == 0:
                # no opener to close
                return False
            else: 
                # current closer doesn't match most urgent
                opener = stack.pop()
                # if c != urgent_par:
                if not self.matchesOpener(opener, c):
                    return False
        return len(stack) == 0;
    
    def isOpener(self, c: str) -> bool:
        opener = c == '(' or c == '{' or c == '['
        return opener

    def matchesOpener(self, opener: str, closer: str) -> bool:
        correct_closer = self.pairs[opener]
        return closer == correct_closer
