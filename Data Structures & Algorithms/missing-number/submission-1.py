class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xored = 0
        for i in range(len(nums)):
            xored ^= nums[i]
            xored ^= i
            print(xored)
        xored ^= len(nums)
        return xored



        