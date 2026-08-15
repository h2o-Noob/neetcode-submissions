class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ma = 0
        b = 0
        e = 0

        if not s:
            return 0

        seen = set()

        while(e < len(s)):
            if s[e] not in seen:
                ma = max(ma, e - b + 1)
                seen.add(s[e])
                e = e + 1
            else:
                seen.remove(s[b])
                b = b + 1
                
        return ma
                

            

