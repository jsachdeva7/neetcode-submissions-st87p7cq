class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash, where keys are tuples of letter frequencies
        anagrams = {}

        for string in strs:
            letterFrequency = [0] * 26
            for c in string:
                index = ord(c) - ord('a')
                letterFrequency[index] += 1
            letterFrequency = tuple(letterFrequency)
            if letterFrequency not in anagrams:
                anagrams[letterFrequency] = [string]
            else:
                anagrams[letterFrequency].append(string)
        
        return list(anagrams.values())