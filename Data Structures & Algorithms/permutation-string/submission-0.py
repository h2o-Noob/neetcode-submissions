class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s = 0
        e = 0

        vals = {}

        for i in s1:
            vals[i] = vals.get(i, 0) + 1

        while(e < len(s2)):

            if (e - s > len(s1) - 1):
                vals[s2[s]] = vals.get(s2[s], 0) + 1
                s += 1
            else:
                vals[s2[e]] = vals.get(s2[e], 0) - 1

                if all(value == 0 for value in vals.values()):
                    return True
        
                e += 1
        
        return False

                




            

