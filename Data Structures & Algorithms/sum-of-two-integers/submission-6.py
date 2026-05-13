class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        slot = 0
        returned = 0
        for i in range(32):
            curA = a >> i
            curB = b >> i
            if curA % 2 == curB % 2 == 1:
                if carry:
                    returned |= (1 << i)
                    carry = 1 
                else:
                    carry = 1
            elif curA % 2 == curB % 2 == 0:
                if carry:
                    returned |= (1 << i)
                carry = 0
            else: # one of them is 1
                if carry:
                    carry = 1
                else:
                    returned |= (1 << i)
                    carry = 0
        if (returned >> 31) % 2 == 1: # python negative number handling
            returned = ~(returned ^ 0xFFFFFFFF)

        return returned