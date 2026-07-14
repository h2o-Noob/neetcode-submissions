class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_s = {}

        for lett in s:
            hash_s[lett] = hash_s.get(lett, 0) + 1


        for lett in t:
            
            if lett not in hash_s:
                return False
        
            hash_s[lett] -= 1

            if hash_s[lett] < 0:
                return False
        
        return True
        