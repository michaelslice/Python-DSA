import heapq

# In python by default this is a min heap
min_heap = []

heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 90)
heapq.heappush(min_heap, 50)
heapq.heappush(min_heap, 40)
heapq.heappush(min_heap, 10)

# Looking at index 0 we will see the smallest element
print(min_heap[0])

# Popping the smallest element
smallest = heapq.heappop(min_heap)
print(smallest)
    
