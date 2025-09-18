# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):
#         from collections import defaultdict
#         from heapq import heapify, heappush,heappop

#         # 2 hashmaps and 1 heap queue
#         self.taskId_priority_map={}
#         self.taskId_userId_map={}
#         self.priority_queue=[]

#         # retrieving information
#         # self.userId = [n[0] for n in tasks]
#         # self.taskId = [n[1] for n in tasks]
#         # self.priority = [n[2] for n in tasks]

#         # storing info into hashmaps and heap
#         size = len(tasks)
#         # for i in range (size):
#         #     self.taskId_priority_map[self.taskId[i]]=self.priority[i]
#         #     self.taskId_userId_map[self.taskId[i]]=self.userId[i]
#         #     heappush(self.priority_queue, (-self.priority[i],-self.taskId[i])) # -ve for max heap

#         for i in range (size):
#             self.taskId_priority_map[tasks[i][1]]=tasks[i][2]
#             self.taskId_userId_map[tasks[i][1]]=tasks[i][0]
#             # heappush(self.priority_queue, (-tasks[i][2],-tasks[i][1])) # -ve for max heap
#             self.priority_queue.append((-tasks[i][2],-tasks[i][1]))
#         heapify(self.priority_queue)
        
#     def add(self, userId: int, taskId: int, priority: int) -> None:
#         self.taskId_priority_map[taskId]=priority
#         self.taskId_userId_map[taskId]=userId
#         heappush(self.priority_queue,(-priority, -taskId))

#     def edit(self, taskId: int, newPriority: int) -> None:
#         self.taskId_priority_map[taskId]=newPriority
#         heappush(self.priority_queue,(-newPriority, -taskId))
    
#     def rmv(self, taskId: int) -> None:
#         del self.taskId_priority_map[taskId]
#         del self.taskId_userId_map[taskId]

#     # def execTop(self) -> int:
#     #     most_prior = self.priority_queue[0]
#     #     while most_prior[0] != -self.taskId_priority_map[-most_prior[1]] :
#     #         heappop(self.priority_queue)
#     #         most_prior = self.priority_queue[0]
#     #     return self.taskId_userId_map[-most_prior[1]]


#     # def execTop(self) -> int:
#     #     while self.priority_queue:                  # keep checking heap
#     #         most_prior = heappop(self.priority_queue)
#     #         taskId = -most_prior[1]

#     #         # ✅ if task still exists AND priority matches, return it
#     #         if taskId in self.taskId_priority_map and \
#     #         -most_prior[0] == self.taskId_priority_map[taskId]:
#     #             return self.taskId_userId_map[taskId]

#     #         # ❌ else (task not in map or priority mismatch)
#     #         # we just loop again -> heap pops next candidate

#     #     return -1   # heap empty, no valid task

#     def execTop(self) -> int:
#             while self.priority_queue:
#                 most_prior = heappop(self.priority_queue)
#                 taskId = -most_prior[1]

#                 # skip if task is deleted or priority is outdated
#                 if taskId not in self.taskId_priority_map:
#                     continue
#                 if -most_prior[0] != self.taskId_priority_map[taskId]:
#                     continue
                    
#                 return self.taskId_userId_map[taskId]
#             return -1

# # Your TaskManager object will be instantiated and called as such:
# # obj = TaskManager(tasks)
# # obj.add(userId,taskId,priority)
# # obj.edit(taskId,newPriority)
# # obj.rmv(taskId)
# # param_4 = obj.execTop()





# copy paste 
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.t2p = defaultdict(int)
        self.t2u = defaultdict(int)
        self.h = []
        for u,t,p in tasks:
            self.t2p[t] = p
            self.t2u[t] = u
            self.h.append((-p,-t, u))
        heapq.heapify(self.h)
        

    def add(self, u: int, t: int, p: int) -> None:
        heapq.heappush(self.h,(-p, -t, u))
        self.t2p[t] = p
        self.t2u[t] = u
        

    def edit(self, t: int, np: int) -> None:
        self.t2p[t] = np
        u = self.t2u[t]
        heapq.heappush(self.h, (-np,-t,u))
        

    def rmv(self, t: int) -> None:
        del self.t2u[t]
        del self.t2p[t]
        

    def execTop(self) -> int:
        while self.h:
            top = heapq.heappop(self.h)
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