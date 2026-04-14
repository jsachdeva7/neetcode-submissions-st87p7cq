class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Longest substring signals dynamic sliding window
        left = 0

        # Can change k characters means in character map, only k + 1 keys
        letterMap = {}
        maxFreq = 0
        maxLength = 0

        for right in range(len(s)):
            letterMap[s[right]] = letterMap.get(s[right], 0) + 1

            # Check if new maxFreq has changed by adding rightmost character
            maxFreq = max(maxFreq, letterMap[s[right]])

            while (right - left + 1) - maxFreq > k:
                # Adding right will make string need too many replacements, invalid, 
                # need to reset left until fixed and can safely add right
                letterMap[s[left]] -= 1
                left = left + 1
            
            maxLength = max(maxLength, right - left + 1)

        return maxLength              
