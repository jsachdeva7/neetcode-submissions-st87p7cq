class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_key = s[i]
            if s_key in s_hash:
                s_hash[s_key] = s_hash[s_key] + 1
            else:
                s_hash[s_key] = 1
            
            t_key = t[i]
            if t_key in t_hash:
                t_hash[t_key] = t_hash[t_key] + 1
            else:
                t_hash[t_key] = 1
        
        if len(s_hash) != len(t_hash): return False
        for s_key in s_hash:
            if s_key not in t_hash or s_hash[s_key] != t_hash[s_key]:
                return False
            
        return True
            

        