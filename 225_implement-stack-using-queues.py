class MyStack:

    def __init__(self):


    def push(self, x: int) -> None:


    def pop(self) -> int:


    def top(self) -> int:


    def empty(self) -> bool:



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Approach 1:  we take two queues , 
# first queue is for putting obj in,
# second queue is for store history obj. 
# new obj will be puted in the inQueue,then copy the historyQueue to the end of inqueue
# time complexity , push O(n) n is the history obj number, pop and top is O(1)
# Approach 2: we tak one queue
# From the first approach ,we knew that the newest obj should in first, and the history objs have to 
# follow the newst obj
# if we save the history obj number before the newest obj put in
# we can pop the number of history obj, and push one by one to the queue 
# after the newest obj is puted in