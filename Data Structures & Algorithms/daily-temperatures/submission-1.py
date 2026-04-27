class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # temp[i] = temperature on the i'th day
        # # return the number of days until it gets warmer
        # # brute force: O(n^2)
        # returned = [None] * len(temperatures)
        # start = 0
        # while (start < len(temperatures)):
        #     end = start + 1
        #     while (end < len(temperatures)):
        #         if temperatures[end] - temperatures[start] > 0:
        #             returned[start] = end - start
        #             break
        #         end += 1
        #     if (returned[start] is None): # never found hotter day
        #         returned[start] = 0
        #     start += 1
        # return returned

        # stack solution:
        returned = [None] * len(temperatures)
        stack = [] # stack = (index, temp)
        stack.append([0, temperatures[0]])
        i = 1
        while i < len(temperatures):
            back = temperatures[i]
            while((len(stack) > 0) and stack[-1][1] < back):
                top = stack.pop()
                returned[top[0]] = i - top[0] # cur day - index of the day in stack
            stack.append([i, back])
            i += 1
        # clear stragglers from stack
        while len(stack) > 0:
            top = stack.pop()
            returned[top[0]] = 0 # never found a hotter day
        return returned

                # pop from stack
                # fill in its return array value
                # try with next stack element



        


        