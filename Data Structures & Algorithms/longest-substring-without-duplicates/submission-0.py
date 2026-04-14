class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        left = 0
        maxLength = 0
        uniqueLetters = {}
        for right in range(len(s)):
            while s[right] in uniqueLetters:
                del uniqueLetters[s[left]]
                left = left + 1
            uniqueLetters[s[right]] = True
            maxLength = max(maxLength, len(uniqueLetters))
        return maxLength