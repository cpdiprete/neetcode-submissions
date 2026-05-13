class Solution:
    def reverseBits(self, n: int) -> int:
        dup = 0
        mult = 31
        track = None
        while n > 0:
            if n % 2 == 1: # odd number, 1 in the right spot
                print(f"multed: {2 ** mult}")
                dup += 2 ** mult
            mult -= 1
            n = n >> 1
        return dup