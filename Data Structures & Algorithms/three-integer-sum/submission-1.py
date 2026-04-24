def twoSum(target, pivot, nums):
    seen = dict()
    all_matches = []
    output = False
    for i in range(len(nums)):
        if i == pivot: # don't want to consider this one
            continue
        missing_piece = target - nums[i]
        if (missing_piece) in seen:
            output = True
            all_matches.append([nums[i], seen[missing_piece]])
        else:
            seen[nums[i]] = nums[i]
    if output is False:
        return (False, None)
    else:
        return (True, all_matches)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # loop through the array 
        # for each i, perform 2sum on array[i + 1, n] where the target is 0 - array[i]
        output = []
        used = set()
        for i in range(len(nums)):
            adjustedTarget = 0 - nums[i]
            relevant, matchesList = twoSum(adjustedTarget, i, nums)
            if relevant == False:
                continue
            filtered = []
            for match in matchesList:
                tup = tuple(sorted([nums[i], match[0], match[1]]))
                if tup in used:
                    continue
                else:     
                    output.append([nums[i], match[0], match[1]])
                    used.add(tup)
                    # print(used)
        return output

            


        