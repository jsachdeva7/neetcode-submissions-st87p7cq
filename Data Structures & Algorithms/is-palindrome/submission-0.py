class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isAlphanumeric(s[left]):
                left = left + 1
                continue
            elif not self.isAlphanumeric(s[right]):
                right = right - 1
                continue
            
            if s[left] != s[right]:
                return False

            left = left + 1
            right = right - 1
        return True
            

    def isAlphanumeric(self, c: str) -> bool:
        alpha = c >= 'a' and c <= 'z'
        numeric = c >= '0' and c <= '9'

        return alpha or numeric