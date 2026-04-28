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







        # # I could do O(n * log(n)) by binary searching
        # for i in range(len(numbers)):
        #     start = i + 1
        #     # binary search on the rest of the array
        #     end = len(numbers) - 1
             
        #     while (end >= start):
        #         middle = (start + end) // 2
        #         candidate = numbers[i] + numbers[middle]
        #         if (candidate == target):
        #             return [i + 1, middle + 1]
        #         if (candidate > target):
        #             end = middle - 1
        #             continue
        #         else:
        #             start = middle + 1
            



        # # I can do 0(n^2) solution by just looping twice
        # # first = 0
        # # second = 0
        # # for i in range(len(numbers)):
        # #     first = numbers[i]
        # #     for j in range(i + 1, len(numbers)):
        # #         if ((first + numbers[j]) == target):
        # #             return [i + 1, j + 1]
        
        # # # return [0, 0]