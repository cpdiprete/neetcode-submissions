class Solution:
    def countSingle(self, num):
        count = 0
        while num > 0:
            if num % 2 == 1:
                # odd
                count += 1
            num = num >> 1
        return count
    def countBits(self, n: int) -> List[int]:
        bitCount = list()
        for i in range(n + 1):
            bitCount.append(self.countSingle(i))
        return bitCount

        