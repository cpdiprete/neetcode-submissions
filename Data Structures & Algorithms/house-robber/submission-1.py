class Solution:
    def rob(self, nums: List[int]) -> int:
        # I can either rob house i - 1 or house i
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        cash = [None] * len(nums) # cash[i] = max amount of robbed money I could have when at house i

        cash[0] = nums[0]
        cash[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cash[i] = max(cash[i - 1], cash[i - 2] + nums[i]) 
        print(cash)
        return cash[len(nums) - 1]       
        