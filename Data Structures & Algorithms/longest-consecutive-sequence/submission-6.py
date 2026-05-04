class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        # add all nums to a dict for O(1) lookup time
        housed = set(nums)
        for num in housed:
            if (num - 1) in housed:
                continue # this isn't the start of some sequence
            else:
                # this is the start of some sequence, count up for its group size
                seqSize = 1
                while (num + 1) in housed:
                    seqSize += 1
                    num = num + 1
                maxSeq = max(maxSeq, seqSize)
        return maxSeq

