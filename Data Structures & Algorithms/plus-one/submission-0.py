class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        carry = False
        i = len(digits) - 1
        digits[i] += 1
        while i >= 0:
            cur = digits[i]
            if carry:
                cur += 1
                carry = False
            if cur <= 9:
                digits[i] = cur
                return digits
            # else, need to subtract 10 and pass the carry
            carry = True
            digits[i] = cur - 10
            i -= 1
        if carry:
            return [1] + digits
        return digits
        