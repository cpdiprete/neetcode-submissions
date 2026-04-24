class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this is the 2 sum dictionary bullshit
        matches = dict()
        # matches[value] = index, so something later can look for this value and get the idx
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in matches:
                return [matches[difference], i]
            else:
                matches[nums[i]] = i
        