class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 
        freq = dict()
        for item in nums:
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
        buckets = [None] * (len(nums) + 1)
        for number, count in freq.items():
            print(count)
            if buckets[count] is None:
                buckets[count] = [number]
            else:
                buckets[count].append(number)
        filtered = []
        added = 0
        end = len(nums)
        while (end >= 0) and (added < k):
            if buckets[end] is None:
                end -= 1
            else:
                filtered += buckets[end]
                added += len(buckets[end])
                end -= 1
        return filtered
                

