class Solution:
    def isPalindrome(self, s: str) -> bool:
        ln = set("abcdefghijklmnopqrstuvwxyz0123456789")
        s = s.lower()

        k = 0
        j = len(s) - 1

        while k<j:
            if s[k] == s[j]:
                k += 1
                j -= 1
            elif s[k] not in ln:
                k += 1
            elif s[j] not in ln:
                j -= 1
            else:
                return False
        
        return True
        