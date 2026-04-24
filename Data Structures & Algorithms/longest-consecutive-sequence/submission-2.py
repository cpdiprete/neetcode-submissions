class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # feel like this could be similar to 2 sum
        # # lemme just start with an 0(n^2) with O(n) space
        # subSeqDict = dict() # dict[number] = (longest sequence, last addition to sequence)
        # for num in nums:
        #     noMatchFound = True
        #     if num in subSeqDict:
        #         continue # no changes tbh
        #     if (num - 1) in subSeqDict:
        #         newScore = subSeqDict[num - 1] + 1
        #         subSeqDict[num] = newScore # we can make one longer of a sequence
        #         i = num
        #         while (i - 1) in subSeqDict: # propogate to the whole subsequence
        #             subSeqDict[i - 1] = newScore
        #             i -= 1
        #         noMatchFound = False
        #     if (num + 1) in subSeqDict:
        #         noMatchFound = False
        #         # now we need to check if this was the missing link
        #         if num in subSeqDict: # this means it was Just triggered by the last check
        #             firstHalf = subSeqDict[num - 1]
        #             secondHalf = subSeqDict[num + 1]
        #             newScore = firstHalf + secondHalf
        #             barrier = num
        #             while (barrier - 1) in subSeqDict:
        #                 subSeqDict[barrier - 1] = newScore
        #                 barrier -= 1 # trying to find the start of where we need to update the seqeunce
        #         else: # no need to connect
        #             newScore = subSeqDict[num + 1] + 1 # we can make one longer of a sequence
        #             subSeqDict[num] = newScore
        #             barrier = num
        #         barrier = num
        #         while (barrier + 1) in subSeqDict:
        #             subSeqDict[barrier + 1] = newScore
        #             barrier += 1
        #     if noMatchFound:
        #         subSeqDict[num] = 1
        # longest = 0
        # print(subSeqDict)
        # for number, streak in subSeqDict.items():
        #     longest = max(streak, longest)
        # return longest
        # ---------- slight video solution aided answer ----------
        # 
        # make a set of all unique numbers
        # loop through set, checking if num - 1 in set (left neighbor)
        # if so, continue
        # if not, this is the start of a sequence, I can now move right from here, and remove elements from the set after considering them part of this sequence
        unique = set(nums)
        longest = 0
        print(unique)
        for num in nums:
            curSeq = 1
            if (num + 1) not in unique: # this is the end of some sequence
                i = num
                while (i - 1) in unique:
                    unique.remove(i - 1)
                    curSeq += 1
                    i -= 1
            longest = max(longest, curSeq)
            
        return longest

        