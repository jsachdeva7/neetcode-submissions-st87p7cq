class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            encodedStr = encodedStr + str(len(string)) + "#" + string
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        while i < len(s):
            # read length prefix
            j = i
            while s[j] != "#":
                j += 1 # start j after the # and number
            length = int(s[i:j]) # number could be multiple digits
            # read the exact string of that length
            word = s[j + 1 : j + 1 + length]
            decodedStrings.append(word)
            # move pointer forward
            i = j + 1 + length
        return decodedStrings
