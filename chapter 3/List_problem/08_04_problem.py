# Write a program to implement a Queue data structure. Queue is a first in first out(fifo) list, in which addtion takes place at the rear end of the queue and deletion takes place at the from end of the queue

import collections

queue = collections.deque()

queue.append('Sameer')
queue.append('Ajay')
queue.append('Kumar')
queue.append('Rohit')
queue.append('Shoeb')
queue.append('Mohit')
queue.append('Amit')
queue.append('Goyal')
queue.append('Saili')
queue.append('Roshni')
queue.append('Kajal')
queue.append('Amrita')

print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print('----------')

[print(x) for x in queue]