class Solution:
    # def find_head(self, nums):
    #     head = 0
    #     tail = len(nums) - 1
    #     while (head <= tail):
    #         mid = (head + tail) // 2
    #         if nums[head] <= nums[tail]:
    #             return head # this is right
    #         if nums[head] <= nums[mid]:
    #             head = mid + 1
    #         else:
    #             tail = mid - 1
    #     return head
    def find_head(self, nums):
        head = 0
        tail = len(nums) - 1
        
        # Use head < tail because when head == tail, we've found the minimum
        while head < tail:
            mid = (head + tail) // 2
            
            # If mid element is greater than tail element, the pivot 
            # MUST be in the right half (e.g., [4, 5, 6, 1, 2], mid is 6, tail is 2)
            if nums[mid] > nums[tail]:
                head = mid + 1
            # Otherwise, the pivot is in the left half, and mid could be the pivot itself
            else:
                tail = mid
                
        return head

    def search(self, nums: List[int], target: int) -> int:
        offset = self.find_head(nums)
        print(f"offset: {offset}")
        head = 0
        tail = len(nums) - 1
        while (head <= tail):
            mid = (head + tail) // 2
            realMid = (mid + offset) % len(nums)
            if nums[realMid] == target:
                return realMid
            if target < nums[realMid]:
                tail = mid - 1
            else:
                head = mid + 1
        return -1