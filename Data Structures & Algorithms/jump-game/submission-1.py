class Solution:
    # def jump_helper(self, nums, i):
    #     if i >= len(nums) - 1:
    #         # reached the jump point, return True
    #         return True
    #     currentMaxDistance = nums[i]
    #     if (currentMaxDistance == 0):
    #         # print(f"failed at spot = {i}")
    #         return False
    #     jump_destination = i + 1
    #     for j in range(jump_destination, jump_destination + currentMaxDistance):
    #         # print(f"checking spot j= {j}")
    #         if (self.jump_helper(nums, j)):
    #             return True
    #     # print(f"failed at spot = {i}")
    #     return False
        

    def canJump(self, nums: List[int]) -> bool:
        # I can do this with DP no?
        # try to jump as far as possible before backtracking and trying anoher spot
        # return self.jump_helper(nums, 0)


        # 1) Start from the final spot, iterate backwards until I find some point that can jump to this spot
        # 2) Now the new target is this jump point, see if it's possible to get here from an earlier spot too

        end_position = len(nums) - 1
        # I can start from the end, and try to move backwards to find potential paths
        jump_point = len(nums) - 1
        while jump_point > 0:
            jump_reach = nums[jump_point]
            if jump_point + jump_reach >= end_position:
                end_position = jump_point
                jump_point = end_position - 1
            else: # check one spot before instead
                jump_point -= 1
        if jump_point == 0 and jump_point + nums[0] >= end_position:
            return True
        return False
            


        