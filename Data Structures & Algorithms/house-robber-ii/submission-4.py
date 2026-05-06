class Solution:
    def robSlice(self, nums):
        # normal house robber question
        spoils = [None] * len(nums)
        spoils[0] = nums[0]
        spoils[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            spoils[i] = max(spoils[i - 1], spoils[i - 2] + nums[i])
        return spoils[len(nums) - 1]

    def rob(self, nums: List[int]) -> int:
        # at the end of the day, I will either benefit from robbing the first house or the last house
        # I can use the current index to see if I can add this value
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        front = self.robSlice(nums[:len(nums) - 1])
        back = self.robSlice(nums[1::])
        return max(front, back)