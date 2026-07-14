class Solution:
    def isPalindrome(self, s: str) -> bool:
        ln = set("abcdefghijklmnopqrstuvwxyz0123456789")
        s = s.lower()

        k = 0
        j = len(s) - 1

        while k < j:
            while k < j and s[k] not in ln:
                k += 1
            while k < j and s[j] not in ln:
                j -= 1

            if s[k] != s[j]:
                return False

            k += 1
            j -= 1

        return True
