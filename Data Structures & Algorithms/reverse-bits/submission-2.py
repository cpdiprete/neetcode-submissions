class Solution:
    def binaryPrint(self, num):
        printStr = ""
        while num > 0:
            if num % 2 == 1:
                printStr += "1"
            else:
                printStr += "0"
            num = num >> 1
        return printStr
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







        # # find the leftmost 1 (keep a counter of the last shifted 1)
        # i = 1
        # while (dup > 0):
        #     if (dup % 2) == 1:
        #         # update tracker
        #         print(i)
        #         track = i
        #     i += 1
        #     dup = dup >> 1
        # if track is None:
        #     return 0
        # print(f"shift amout: {track}")
        # output = n << (32 - track)
        # print(self.binaryPrint(output))
        # return output

            

        