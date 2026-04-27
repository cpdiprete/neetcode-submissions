class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp[i] = temperature on the i'th day
        # return the number of days until it gets warmer
        returned = [None] * len(temperatures)
        start = 0
        while (start < len(temperatures)):
            end = start + 1
            while (end < len(temperatures)):
                if temperatures[end] - temperatures[start] > 0:
                    returned[start] = end - start
                    break
                end += 1
            if (returned[start] is None): # never found hotter day
                returned[start] = 0
            start += 1
        return returned


        


        