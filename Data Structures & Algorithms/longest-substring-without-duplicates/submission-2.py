class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = dict()
        maxLen = 0
        curLen = 0
        curStart = 0
        # I can loop with a head and a tail through the list
        # subSet[char] = index of the char
            # 1) If s[tail] not in subSet, add it to subSet, add to currentLen and continue
            # 2) if s[tail] is in subset, curLen = old subSet[s[tail]] - tail
                # - compare to maxLen
                # - subSet[s[tail]] = index
                # TODO: how do I account for the ones cut off prior to this repeated char
        # solution is just to move the physical head pointer forward by 1, but then i'd need to recompute the seen dict...
        # I can add to the set and 
        for i in range(len(s)):
            if s[i] not in subSet.keys():
                curLen += 1
            else: # current char is in subSet already
                print(curLen)
                curLen = i - subSet[s[i]] 
                oldStart = curStart
                curStart = subSet[s[i]] + 1 # new subStr start right after the old element
                for j in range(oldStart, curStart):
                    del subSet[s[j]] # need to prune our tracked set
                print(curLen)
                print("------")
            subSet[s[i]] = i
            maxLen = max(maxLen, curLen)
        return maxLen

        