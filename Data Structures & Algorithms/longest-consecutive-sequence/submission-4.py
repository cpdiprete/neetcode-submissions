class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     unique = set(nums)
    #     longest = 0
    #     print(unique)
    #     for num in nums:
    #         curSeq = 1
    #         if (num + 1) not in unique: # this is the end of some sequence
    #             i = num
    #             while (i - 1) in unique:
    #                 unique.remove(i - 1)
    #                 curSeq += 1
    #                 i -= 1
    #         longest = max(longest, curSeq)
    #     return longest
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        # add all nums to a dict for O(1) lookup time
        housed = dict()
        for num in nums:
            housed[num] = 0
        for num in housed.keys():
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

