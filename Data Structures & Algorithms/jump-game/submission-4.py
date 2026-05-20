class Solution:
    def canJump(self, nums: List[int]) -> bool:
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
            


        