import numpy as np
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 
        c = collections.Counter(nums)
        r = list(c.most_common(k))
        d = [n1 for (n1, n2) in r]
        print(d)
        return list(d)
