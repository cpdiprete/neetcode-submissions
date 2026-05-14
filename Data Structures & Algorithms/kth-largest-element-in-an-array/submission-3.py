class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if I keep a running stack, I can iterate once and add/remove
        # idea: if I keep a minStack of size (n - k), then the min of the item's removed or ignored from the stack will be our value
        ignored = []
        noneCount = len(nums) - k - 1 # shifted left by 1 for 0 indexing

        largest = -1001
        largestIndex = None

        stack = [1001] * (len(nums) - k)
        # stack = [largest, 2nd largest, ..., smallest]
        for i in range(len(nums)):
            # print(f"ignored: {ignored} | largest: {largest} | largestIndex: {largestIndex}")
            num = nums[i]
            if noneCount >= 0:
                if num > largest:
                    largest = num
                    largestIndex = i
                stack[i] = num
                noneCount -= 1
                continue
            if num >= largest:
                ignored.append(num)
            else:
                # need to replace largest element in minStack
                # also need to find the new largest
                ignored.append(largest)
                stack[largestIndex] = num
                largest = -1001
                for j in range(len(stack)):
                    if stack[j] > largest:
                        largest = stack[j]
                        largestIndex = j
        # print(ignored)
        return min(ignored)
                




            # 1) if num < minVal:  
            # if this number is larger than the current smallest element

        