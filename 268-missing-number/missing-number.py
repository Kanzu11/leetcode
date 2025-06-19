class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)+1
        for i in range(x):
            if not i in nums:
                return i