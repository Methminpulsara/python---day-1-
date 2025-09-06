class QueueError:
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, element):
        self.__queue.insert(0, element)

    def dequeue(self):
        if self.is_empty():
           raise QueueError("Queue is Empty")
        val = self.__queue[-1]
        del self.__queue[-1]
        return val

    def is_empty(self):
        return len(self.__queue) == 0

    def get_queue(self):
        return list(self.__queue)
q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

#
# print(q1.get_queue())

try:
    print(q1.dequeue())
    print(q1.dequeue())
except QueueError as e :
    print(e)
finally:
    print(q1.get_queue())
