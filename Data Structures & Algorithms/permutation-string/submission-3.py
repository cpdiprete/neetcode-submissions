class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        s1 = sorted(s1)
        while (i + len(s1)) <= len(s2):
            if (sorted(s2[i:i + len(s1)]) == s1):
                return True
            else:

                i += 1
        return False
        # windowSize = len(s1)
        # windowChars = dict()
        # for c in s1:
        #     if c not in windowChars:
        #         windowChars[c] = 1
        #     else:
        #         windowChars[c] += 1
        # # now I have the number of chars that a subwindow would need
        # i = 0
        # curDict = windowChars.copy() # make a copy
        # while i < len(s2):
        #     print(f"current char index: {i}")
        #     if not curDict: # we finished finding the substring
        #         return True
        #     if s2[i] not in curDict:
        #         print(f"dict before reset: {curDict}")
        #         curDict = windowChars.copy()
        #         print(f"reset curdict: {windowChars}")
        #     else:
        #         if curDict[s2[i]] <= 1:
        #             del curDict[s2[i]]
        #         else:
        #             curDict[s2[i]] -= 1
        #         if not curDict: # we finished finding the substring
        #             return True
        #     i += 1
        # return False


            

                

        # # d1 = dict()
        # # d2 = dict()
        # # for c in s1:
        # #     if c not in d1:
        # #         d1[c] = 1
        # #     else:
        # #         d1[c] += 1
        # # for c in s2:
        # #     if c not in d2:
        # #         d2[c] = 1
        # #     else:
        # #         d2[c] += 1
        
        # # for character, count in d1.items():
        # #     if d2[character] < count:
        # #         return False
        # # return True


        