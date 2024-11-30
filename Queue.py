class QueueReplica:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.MAX_QUEUE_SIZE = 100
        self.queue = [0] * self.MAX_QUEUE_SIZE

    def IsEmptyQ(self):
        return self.front == -1 or self.front > self.rear

    def IsFullQ(self):
        return self.rear == self.MAX_QUEUE_SIZE - 1


    def Enqueue(self, item):
        if self.IsFullQ():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item

    def Dequeue(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1

    def Peek(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        return self.queue[self.front]

    def Show(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        print("Queue items:")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i])

    def ReverseQueue(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        rq = QueueReplica()
        a = []
        for i in range(self.front, self.rear + 1):
            a.append(self.queue[i])

        for j in reversed(a):
            rq.Enqueue(j)

        return rq                
    

def main():

    my_queue = QueueReplica()
    my_queue.Enqueue(1)
    my_queue.Enqueue(2)
    my_queue.Enqueue(3)
    my_queue.Enqueue(4)
    my_queue.Enqueue(5)
    my_queue.Show()
    my_queue.Dequeue()
    my_queue.Show()
    rq = QueueReplica()
    rq = my_queue.ReverseQueue()
    rq.Show()

if __name__ == "__main__":
    main()