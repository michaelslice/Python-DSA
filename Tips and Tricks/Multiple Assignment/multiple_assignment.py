'''
We can do multiple assignment in 1 line!

For example...

self.key = key, and self.val = val
'''
class Node:
    def __init__(self, key, val) -> None:  
        self.key, self.val = key, val
        self.prev = self.next = None