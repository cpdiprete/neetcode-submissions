class Solution:
    def backtrack(self, nums, subset):
        if len(nums) == 0:
            self.subs.append(subset)
            return subset
        self.backtrack(nums[1:], [nums[0]] + subset)
        self.backtrack(nums[1:], subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subs = []
        print(self.backtrack(nums, []))
        return self.subs
        