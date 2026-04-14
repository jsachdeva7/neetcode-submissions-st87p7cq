class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for i in range(len(s)):
            sLetter = s[i]
            tLetter = t[i]

            if sLetter not in freq:
                freq[sLetter] = 1
            else:
                freq[sLetter] = freq[sLetter] + 1
            
            if tLetter not in freq:
                freq[tLetter] = -1
            else:
                freq[tLetter] = freq[tLetter] - 1
        
        for letter in freq:
            if freq[letter] != 0:
                return False

        return True
        