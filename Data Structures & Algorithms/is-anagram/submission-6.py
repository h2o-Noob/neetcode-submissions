class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        hash_s = {}

        for l in s:
            hash_s[l] = hash_s.get(l, 0) + 1
        for l in t:
            hash_s[l] = hash_s.get(l,0) - 1
        for l in s:
            if hash_s[l] != 0:
                return False
        return True
        


        

        