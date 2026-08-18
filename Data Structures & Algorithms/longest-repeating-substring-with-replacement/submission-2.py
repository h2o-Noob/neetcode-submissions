class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        b = 0
        e = 0
        ma = 0

        count = defaultdict(int)

        while e < len(s):

            count[s[e]] += 1

            while (e - b + 1) - max(count.values()) > k:
                count[s[b]] -= 1
                b += 1

            ma = max(ma, e - b + 1)
            e += 1

        return ma
