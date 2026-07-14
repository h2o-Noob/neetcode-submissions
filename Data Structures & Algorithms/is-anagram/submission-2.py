class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        for lett in s:
            hash_s[lett] = hash_s.get(lett, 0) + 1
        for lett in t:
            hash_s[lett] = hash_s.get(lett, 0) - 1
        for lett in s:
            if hash_s[lett] > 0:
                return False
        for lett in t:
            if hash_s[lett] < 0:
                return False
        return True
        
        
        
        