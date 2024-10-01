from collections import deque
# Lists can also be used as queues
# FIFO

queue = deque(["Joe", "Michael", "Evan"])
queue.append("Eric")
queue.append("Steven")
queue.popleft()
print(queue)