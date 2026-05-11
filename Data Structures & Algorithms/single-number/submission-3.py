class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initialize an empty set
        # loop through the list, add to the set, or remove from the set if presetn
        # return the element left in the set
        track = 0
        for num in nums:
            track = track ^ num
        print(track)
        return track