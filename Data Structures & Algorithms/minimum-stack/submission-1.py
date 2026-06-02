class MinStack:

    # idea is to maintain 2 different stacks:
    # 1) Stack with the current min element at the top
    # 2) Stack with the most recent element at the top
    # the whole purpose of the minstack is to track what the min is at this point in time,
    # every single insertion will include either an insertion of the new element, or the current min
    # 1) if it's smaller, I remove the 

    def __init__(self):
        self.size = 0
        self.backing = []
        self.mini = []

        
    def push(self, val: int) -> None:
        self.size += 1
        self.backing.append(val)
        if (len(self.mini) == 0):
            self.mini.append(val)
        elif self.mini[len(self.mini) - 1] < val:
            # repeat our last mini
            self.mini.append(self.mini[len(self.mini) - 1])
        else:
            self.mini.append(val)
    def pop(self) -> None:
        if len(self.backing) == 0:
            return
        self.backing.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.backing[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]
        
