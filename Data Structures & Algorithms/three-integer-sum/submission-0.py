class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        seen = set()

        for k, num in enumerate(nums):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                sum = nums[i] + nums[j]
                if sum + num == 0:
                    seen.add((nums[i], num, nums[j]))
                if sum + num > 0:
                    j -= 1
                else:
                    i += 1
        return list(seen)


        

        