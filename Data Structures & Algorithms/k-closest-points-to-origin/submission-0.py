import math
import heapq
class Solution:
    def getDistance(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        mappings = dict()
        for x, y in points:
            dist = self.getDistance(x, y)
            # add to the minQueue
            distances.append(dist)
            if dist not in mappings:
                mappings[dist] = [[x, y]]
            else:
                mappings[dist].append([x, y])
        heapq.heapify(distances)
        returnList = []
        count = 0
        while (count < k):
            top = heapq.heappop(distances)
            returnList.append(mappings[top][0])
            if len(mappings[top]) > 1:
                mappings[top] = mappings[top][1::]
            count += 1
        # print(returnList)
        return returnList