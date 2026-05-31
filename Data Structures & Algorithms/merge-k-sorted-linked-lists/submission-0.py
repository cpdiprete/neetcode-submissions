# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def prune(self, heads):
        oglen = len(heads)
        pruneList = []
        for i in range(len(heads)):
            if heads[i] is None:
                pruneList.append(i)
        offset = 0
        for ind in pruneList:
            heads.pop(ind + offset)
            offset -= 1
        if len(heads) != oglen:
            print("actually pruned smth") 
        return heads


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newHead = None
        headToUpdate = None
        # loop through all heads, find the minimal one and set newHead to that one
        smallest = 1001
        for i in range(len(lists)):
            head = lists[i]
            if head is None:
                continue
            if head.val <= smallest:
                newHead = head
                smallest = head.val
                headToUpdate = i
        # return newHead
        if not headToUpdate is None:
            if lists[headToUpdate].next:
                lists[headToUpdate] = lists[headToUpdate].next
            else:
            # remove from the list
                lists.pop(headToUpdate)   
        headToReturn = newHead
        # I have the head of my merged list, and a list of pointers to all of the other heads
        # while there are valid pointers, I need to get the 
        iters = 0
        while True:
            # if iters > 10:
            #     return None
            # iters += 1

            # prune the elements of the list that are None
            lists = self.prune(lists)
            if len(lists) == 0:
                return headToReturn
            mini = 1001
            headToUpdate = None
            for i in range(len(lists)):
                head = lists[i]
                if head.val <= mini:
                    mini = head.val
                    headToUpdate = i
            if headToUpdate is None:
                print("nothing to update")
            # else:
                # print(f"updating lists[{headToUpdate}] = {lists[headToUpdate].val}")

            if lists[headToUpdate].next is None:
                print("reached end")
            newHead.next = lists[headToUpdate]
            if lists[headToUpdate].next:
                print(f"stepping forward: lists[{headToUpdate}] | {lists[headToUpdate].val} ----> {lists[headToUpdate].next.val}")
            lists[headToUpdate] = lists[headToUpdate].next
            newHead = newHead.next # move forward
        
            


