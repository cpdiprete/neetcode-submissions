import heapq

class CalvinsHeap:
    # I need some object that can 
    # 1) order new and existing elements by max priority
    # 2) add some way to bench elements for some cooldown
    # 2) maintain the number of cycles that have run overall so far
    def __init__(self, cooldown):
        self.cooldown = cooldown
        self.heap = [] # heap[i] = [priority, taskName]
        heapq.heapify(self.heap)
        self.bench = [] # bench[i] = [remaining cooldown time for this task, task]
        heapq.heapify(self.bench)
        self.cycles = 0
    def add_tasks(self, counter):
        for taskchar, count in counter.items():
            heapq.heappush(self.heap, (count * -1, taskchar)) # order them based on task priority, invert for max heap
    def clear_bench(self):
    # Pull any items off bench that have sat long enough
        if len(self.bench) == 0:
            return False # no item to clear
        while (len(self.bench) > 0):
            if self.bench[0][0] == self.cycles: # put this back into play
                top = heapq.heappop(self.bench)
                heapq.heappush(self.heap, (top[1], top[2])) # push [priority, task] back onto task heap
            else: # don't need to clear any bench members left
                return False
    def run_task(self):
        # print(f"run_task i = {self.cycles} | tasks = {self.heap} | bench = {self.bench}")
        # run a task
        # return False if no tasks need to be run
        # return True if a task was run
        if len(self.heap) == 0 and len(self.bench) == 0:
            return False
        self.cycles += 1
        if len(self.heap) == 0:
            self.clear_bench()
            return True
        top = heapq.heappop(self.heap) # get the top element (priority, task)
        priority = top[0] + 1
        if priority != 0:
        # need to bench this to run later again
            heapq.heappush(self.bench, (self.cooldown + self.cycles, priority, top[1]))
        # now we can pull any items into play from the bench that have sat long enough
        self.clear_bench()
        return True

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # I can maintain some other data structure for items that can be put on hold
        # 1) go through the task list, and use a dict to track the frequency of the item
        # 2) make a Heap based on the priority
        # 3) make a heap for the benched values, and after each cycle check if anything needs to be popped off the top

        # each task takes 1 cycle to finish
        # give each letter a priority, the one with most duplicates should be ran first
        prios = dict()
        for task in tasks:
            if task in prios:
                prios[task] += 1
            else:
                prios[task] = 1
        Task_obj = CalvinsHeap(n)
        Task_obj.add_tasks(prios)
        while Task_obj.run_task():
            # print("running task from main loop")
            continue
        return Task_obj.cycles