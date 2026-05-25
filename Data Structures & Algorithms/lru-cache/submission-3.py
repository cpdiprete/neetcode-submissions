
class DLL_Node:
    def __init__(self, key, val = None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        # what if I made a dictionary that mapped dict[key] = LL_node(), and maintain a tail pointer... this way: 
        # get(): 
        #   a) update dict[key].prev.next = dict[key].next, and dict[key].next.prev = dict[key].prev
        #   b) update tail.next = dict[key], and dict[key].prev = tail, dict[key].next = None
        self.backing = dict()
        self.capacity = capacity
        self.tail = None
        self.head = None
    def __repr__(self):
        cur = self.head
        rStr = ""
        while cur:
            rStr += f"[Key: {cur.key}|Val: {cur.val}]--> "
            cur = cur.next
            # there's an infinite loop somewhere
        rStr += "None"
        return rStr
    def access_update(self, node):
        if self.tail == node: # I probably need to implement this __==__ operator in my class?
            return self.head# no need to update this if it's alr the tail
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        elif node.next:
            # this node doesn't have a prev pointer, it must be the head!
            
            self.head = node.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        elif not node.next and not node.prev:
            # this is a new node
            node.prev = tail
            node.next = None
            self.tail.next = node
            self.tail = node
        return self.head
    def get(self, key: int) -> int:
        print(self)
        # print(self)
        # O(1) access for the value of this key, This is easy to use a backing dict
        if key not in self.backing:
            return -1
        node = self.backing[key]
        self.access_update(node)
        return self.backing[key].val
        
    def put(self, key: int, value: int) -> None:
        # O(1) time to update the value of this key-value pair. If this causes size
        # to surpass capacity, evict the LRU
        if key in self.backing:
            # no need to evict, just update order
            node = self.backing[key]
            node.val = value
            self.access_update(node)
            return
        new_node = DLL_Node(key, value) 
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
            self.backing[key] = new_node
            
            return
        # to get here, the item is not yet in the dict, must make a new node and see if eviction is neccessary
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.backing[key] = new_node
        if len(self.backing) <= self.capacity:
            return
        else:
            del self.backing[self.head.key]
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            


        
