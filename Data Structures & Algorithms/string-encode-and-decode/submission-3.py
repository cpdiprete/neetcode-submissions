class Solution:
    # the key idea is some consisitent way of knowing when the end of the string should be
    # I can do this with some split characte that encoded the length
    # eg. "3&cal6&dorked"
    def encode(self, strs: List[str]) -> str:
        rstr = ""
        for st in strs:
            length = len(st)
            # need to know some way when the length value is startin
            rstr += f"{length}^{st}"
        print(rstr)
        return rstr
        

    def decode(self, s: str) -> List[str]:
        rList = []
        start = s.find("^") # to get the end of our original length
        if (start == -1):
            return []
        curLengthEncoding = int(s[0:start]) # the length of our next encoded string after the carrot
        i = start
        while (i < len(s)):
            if (i + curLengthEncoding + 1) == len(s):
                piece = s[i + 1::]
                rList.append(piece)
                print(piece)
                break
            piece = s[i + 1: i + curLengthEncoding + 1] # get the actual substring
            rList.append(piece)
            print(piece)
            start = s[(i + curLengthEncoding + 1)::].find("^") # to get the slot after our next number string
            start += (i + curLengthEncoding + 1)
            if start == -1:
                break
            # print(f"debug: {s[i + curLengthEncoding + 1: start]}")
            curLengthEncoding = int(s[i + curLengthEncoding + 1: start]) # the next integer
            i = start # reset i 
        return rList
