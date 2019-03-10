#Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is called a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap. It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.

import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
# Add element
# Inserting a data element to a heap always adds the element at the last index.
heapq.heappush(H,8)
print(H)
# Remove element from the heap
# You can remove the element at first index by using this function. In the below example the function will always remove the element at the index position 1.
heapq.heappop(H)

print(H)

# Replace an element
# The heapreplace function always removes the smallest element of the heap and inserts the new incoming element at some place not fixed by any order.
heapq.heapreplace(H,6)
print(H)

