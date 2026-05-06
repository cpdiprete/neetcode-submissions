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
        # # I either rob the first house or not, I can pass in a linear robbery problem wihout the first slice and another without the last, and return the max

        # greedySpoils = [None] * len(nums)
        # patientSpoils = [None] * len(nums)

        # greedySpoils[0] = nums[0]
        # patientSpoils[0] = 0
        
        # greedySpoils[1] = nums[0] # just robbed from front, can't rob here
        # patientSpoils[1] = nums[1] # didn't rob from from front, take this now
        # for i in range(2, len(nums) - 1):
        #     patientSpoils[i] = max(patientSpoils[i - 1], patientSpoils[i - 2] + nums[i])
        #     greedySpoils[i] = max(greedySpoils[i - 1], greedySpoils[i - 2] + nums[i])
        # greedySpoils[len(nums) - 1] = greedySpoils[len(nums) - 2]
        # patientSpoils[len(nums) - 1] = max(patientSpoils[len(nums) - 2], patientSpoils[len(nums) - 3] + nums[len(nums) - 1])
        # # print(f"greed: {greedySpoils[len(nums) - 1]}")
        # # print(f"patient: {patientSpoils[len(nums) - 1]}")
        # return max(patientSpoils[len(nums) - 1], greedySpoils[len(nums) - 1])

