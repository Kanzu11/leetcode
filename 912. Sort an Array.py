class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        pivot = random.choice(nums)

        left = [i for i in nums if pivot > i]
        middle = [i for i in nums if pivot == i]
        right = [i for i in nums if pivot < i]

        return self.sortArray(left) + middle + self.sortArray(right)
