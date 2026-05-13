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
        if (returned >> 31) % 2 == 1:
            returned = ~(returned ^ 0xFFFFFFFF)

        # if carry:
        #     returned |= (1 << i + 1)
        return returned


                
                


        while a > 0 and b > 0:
            # if both are 0's
            if (a % 2 == 0 and b % 2 == 0):
                if carry == 1:
                    # this spot is 
                    carry = 0
                    returned |= (1 << slot) # basically add this 1 to the right spot
            elif a % 2 == 0:
                # if carry is true we need to zero out this slot and set carry to 0
                if carry == 1:
                    carry = 1 # we pass this along to the next
                else:
                    returned |= (1 << slot)
            elif b % 2 == 0:
                if carry == 1:
                    carry = 1 # we pass this along to the next
                else:
                    returned |= (1 << slot)
            else: # both are 1, need to carry check big time
                if carry == 1:
                    returned |= (1 << slot)
                    carry = 1
                else:
                    carry = 1
            slot += 1
            a = a >> 1
            b = b >> 1
        while a > 0:
            if a % 2 == 0:
                if carry == 1:
                    returned |= (1 << slot)
                    carry = 0
                else:
                    pass
            else:
                if carry == 1:
                    carry == 1# 
                else:
                    carry = 0
                    returned |= (1 << slot)
            a >>= 2
        while b > 0:
            if b % 2 == 0:
                if carry == 1:
                    returned |= (1 << slot)
                    carry = 0
                else:
                    pass
            else:
                if carry == 1:
                    carry == 1# 
                else:
                    carry = 0
                    returned |= (1 << slot)
            b >>= 2
        if carry == 1:
            returned |= (1 << slot)
        return returned

                    
        