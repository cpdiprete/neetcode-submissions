class LLnode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class LL:
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size
    def add_node(self, value_to_add):
        if not self.head:
            self.head = LLnode(value_to_add, None)
        else:
            if value_to_add < self.head.val:
                newNode = LLnode(value_to_add, self.head)
                self.head = newNode
                self.size += 1
                return
            lag = self.head
            scout = self.head.next
            iters = 0
            while (scout and scout.val < value_to_add):
                lag = lag.next
                scout = scout.next
            # now that I've broken here, I need lag to point to a new node, which points to scout
            newNode = LLnode(value_to_add, scout)
            lag.next = newNode
        self.size  += 1
    def print_tree(self):
        head = self.head
        printStr = ""
        while head:
            printStr += str(head.val) + "->"
            head = head.next
        printStr += "None"
        print(printStr)

    def get_median(self):
        median = self.head
        lag = None
        curIndex = 0
        index = 0
        self.print_tree()
        if self.size == 1:
            return median.val
        while curIndex < (self.size // 2):
            curIndex += 1
            lag = median
            median = median.next

        if (self.size % 2) == 0:
            return (median.val + lag.val) / 2
        else:
            return median.val

class MedianFinder:

    def __init__(self):
        self.linked = LL()

    def addNum(self, num: int) -> None:
        self.linked.add_node(num)

    def findMedian(self) -> float:
        return self.linked.get_median()
        
        