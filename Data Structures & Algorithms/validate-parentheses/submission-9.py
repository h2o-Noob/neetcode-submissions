class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        
        sign = []
        link = {"}" : "{", "]" : "[", ")": "("}

        for l in s:
            if l in link.values():
                sign.append(l)
            elif sign and sign[-1] == link.get(l):
                sign.pop()
            else:
                return False
        
        if not sign:
            return True
        else:
            return False

        


        