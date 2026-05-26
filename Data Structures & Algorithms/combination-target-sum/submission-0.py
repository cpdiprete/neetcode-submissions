class Solution:
    def __init__(self):
        self.subPaths = []
    def recurse(self, nums, target, runningSum, path, subPaths):
        if runningSum == target:
            return path
        for i in range(len(nums)):
            num = nums[i]
            if (runningSum + num) <= target:
                branch = self.recurse(nums[i::], target, runningSum + num, path + [num], subPaths)
                if branch is not None:
                    subPaths.append(branch)
                # subPaths.append([self.recurse(nums[i::], target, runningSum + num, path + [num], subPaths)])
        self.subPaths = subPaths
        
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        paths = self.recurse(nums, target, 0, [], [])
        print(self.subPaths)
        return self.subPaths
        
        