class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 0
        for i in range(len(numbers)):
            first = numbers[i]
            for j in range(i + 1, len(numbers)):
                if ((first + numbers[j]) == target):
                    return [i + 1, j + 1]
        
        # return [0, 0]