class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for items in nums:
            table[items] = table.get(items, 0) + 1

        for items in table:
            if table[items] > 1:
                return True
        
        return False
        