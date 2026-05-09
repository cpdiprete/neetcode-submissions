class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        firstChar = dict()
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True # its possible to make empty dict
        for i in range(1, len(s) + 1):
            for j in range(i):
                # if we could make words at point j, and if s[j->i] is a word, then we're all good here too
                if (dp[j] and s[j:i] in wordSet):
                    dp[i] = True # we can make this word
                    break
        print(dp)
        return dp[len(s)]
        