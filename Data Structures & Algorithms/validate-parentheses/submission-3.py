from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            c = s[i]
            if c not in [")", "]", "}"]:
                print(c)
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            top = stack.pop()
            # print(top)
            if c == "]":
                if top != "[":
                    return False
            elif c == ")":
                if top != '(':
                    return False
            elif c == "}":
                if top != '{':
                    return False
        # print(stack)
        return (len(stack)== 0)



        