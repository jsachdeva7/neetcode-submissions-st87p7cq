class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make character frequency map of s1
        s1Map = {}
        for c in s1:
            if c not in s1Map:
                s1Map[c] = 1
            else:
                s1Map[c] = s1Map[c] + 1

        # iterate through s2
        left = 0
        s2Map = {}
        for right in range(len(s2)):
            if s2[right] not in s1Map:
                # Need to get past right most letter, ruining substring
                s2Map.clear()
                left = right + 1
            else:
                # Letter is in s1
                if s2[right] not in s2Map:
                    s2Map[s2[right]] = 1
                else:
                    s2Map[s2[right]] += 1
                    while s2Map[s2[right]] > s1Map[s2[right]]:
                        # Num occurences of letter in current s2 substring
                        # is too many, need to move left pointer until
                        # occurences match with s1
                        s2Map[s2[left]] -= 1
                        if s2Map[s2[left]] == 0:
                            # Remove from map if no more occurences
                            del s2Map[s2[left]]
                        left = left + 1
            if right - left + 1 == len(s1):
                if s2Map == s1Map:
                    return True
                s2Map[s2[left]] -= 1
                if s2Map[s2[left]] == 0:
                    # Remove from map if no more occurences
                    del s2Map[s2[left]]
                left = left + 1
        return False