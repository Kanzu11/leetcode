class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 0
        n = len(nums)
        for i in range(n):
            for j in range(1+i,n):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    c+=1
        return c