class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = 0
        # I can either start from back (this makes more sense bc we won't have to check ahead for blockages, just passing them back)
        # or the front
        # sort by position, but I need to keep them attached
        # with input data, I know the time to end goal
        zipped = [[position[i], speed[i]] for i in range(len(position))]
        zipped.sort(key = lambda x: x[0])
        print(zipped)
        
        groups = 0
        currentLag = -1 # infinite to start for kaboose
        i = len(zipped) - 1
        while (i >= 0):
            delay = (target - zipped[i][0]) / zipped[i][1]
            if delay > currentLag: # this will finish unblocked, this is the new kaboose
                groups += 1
                currentLag = delay
            i -= 1
        return groups

        
