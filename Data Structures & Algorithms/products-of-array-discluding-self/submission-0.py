# import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        multiplied = []
        # O(n) using division
        total = 1
        zeroCount = 0
        zeroSpot = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if zeroCount > 0:
                    # impossible to get non-zero value
                    return [0 for _ in  range(len(nums))]
                zeroCount += 1
                zeroSpot["zero"] = i
                continue
            else:
                total *= num
        if zeroCount == 1:
            multiplied = [0 for _ in  range(len(nums))]
            multiplied[zeroSpot["zero"]] = total
        else:
            for num in nums:
                multiplied.append(int(total / num))
        return multiplied

        