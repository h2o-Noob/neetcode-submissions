class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set("qwertyuioplkjhgfdsazxcvbnm0987654321")

        f = 0
        l = len(s) - 1

        ns = s.lower()

        while f < l:
            if ns[f] not in valid:
                f = f + 1
            elif ns[l] not in valid:
                l = l - 1
            elif ns[f] != ns[l]:
                return False
            else:
                l = l - 1
                f = f + 1
        
        return True


        