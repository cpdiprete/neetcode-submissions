# def bsearch(start, arr, target):
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            if numbers[head] + numbers[tail] == target:
                return [head + 1, tail + 1]
            elif numbers[head] + numbers[tail] > target:
                tail -= 1
            else:
                head += 1