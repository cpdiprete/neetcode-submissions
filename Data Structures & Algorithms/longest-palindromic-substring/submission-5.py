class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSeen = ""
        for i in range(len(s)):
            # treat i like the center
            curStreak = ""
            start = i
            end = i
             # oddCheck
            while (start >= 0 and end < len(s)):
                if s[start] != s[end]:
                    break
                if start == end:
                    curStreak = s[start]  
                else:
                    curStreak = s[start:end + 1]
                start -= 1
                end += 1
            if len(curStreak) > len(maxSeen):
                maxSeen = curStreak

            curStreak = ""
            end = i + 1
            start = i 
            while (start >= 0 and end < len(s)):
                # the center is basically i
                if s[start] != s[end]:
                    break
                curStreak = s[start:end + 1]
                start -= 1
                end += 1
            if len(curStreak) > len(maxSeen):
                maxSeen = curStreak
        return maxSeen