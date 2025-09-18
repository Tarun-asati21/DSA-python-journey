class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        from collections import defaultdict
        from heapq import heapify, heappush,heappop

        # 2 hashmaps and 1 heap queue
        # Notation = {t:taskid, u:userid , p:priority}
        self.t2p = defaultdict(int)
        self.t2u = defaultdict(int)
        self.hq = []
        for u,t,p in tasks:
            self.t2p[t] = p
            self.t2u[t] = u
            self.hq.append((-p,-t, u))  # -ve for max heap
        heapify(self.hq)
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.t2p[taskId]=priority
        self.t2u[taskId]=userId
        heappush(self.hq,(-priority, -taskId,userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.t2p[taskId]=newPriority
        userId = self.t2u[taskId]
        heappush(self.hq,(-newPriority, -taskId, userId ))
    
    def rmv(self, taskId: int) -> None:
        del self.t2p[taskId]
        del self.t2u[taskId]

    def execTop(self) -> int:
        while self.hq:
            top = heappop(self.hq)
            p, t, u = -top[0], -top[1], top[2]
            if t in self.t2p.keys() and self.t2p[t] == p and self.t2u[t] == u:
                self.rmv(t)
                return u
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()