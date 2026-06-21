class Solution:
#   Observations: 
# 1) a group of 2 letters may be mapped together if (the number they make is > 0 and <= 26, it doesn't lead with a 0)
# 2) at a new letter, it will 


    def numDecodings(self, s: str) -> int:
        if len(s) < 1 or s[0] == "0":
            return 0
        dp = [None] * len(s)
        dp[0] = 1 # getting here means its possible to map the first element to a valid char
        for i in range(1, len(s)):
            # if it's 0, we can't map this number unless the prev number is 2 or 1
            c = int(s[i])
            if c == 0:
                if int(s[i-1]) > 2 or int(s[i-1]) == 0:
                    return 0 # this has created an impossible mapping
                # TODO: This could actually eat up an extra grouping if it forces the prev to map to it to stay alive. We need to check if the prev was double counted and adjust
                if i >= 2 and int(s[i-2]) <= 2: # we double counted and need to downgrade for this life save
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1]
                continue # this wouldn't stand alone
            print(f"reached check for group at i = {i}")
            # To reach this point, our number is between 1 and 6, meaning we need to check it's predecessor for an addition
            newP = dp[i-1]
            if int(s[i-1]) > 0 and int(s[i-1]) < 3: # this could be grouped with this char
                if c > 6 and int(s[i-1]) == 2:
                    # can't map double, same as the prev
                    dp[i] = newP
                    continue
                if i > 1:
                    newP += dp[i-2]
                else:
                    newP += dp[i-1]
            dp[i] = newP
        print(dp)
        return dp[len(s)-1]
            
        
