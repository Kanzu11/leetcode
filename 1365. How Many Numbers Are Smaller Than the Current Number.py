class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        n = sorted(nums)
        for i in range(len(nums)):
            a.append(n.index(nums[i]))
        return a
