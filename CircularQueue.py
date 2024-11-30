class CircularQueue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.MAX_QUEUE_SIZE = 100
        self.queue = [0] * self.MAX_QUEUE_SIZE

    def IsFullQ(self):
        return (self.rear + 1) % self.MAX_QUEUE_SIZE == self.front

    def IsEmptyQ(self):
        return self.front == -1

    def Enqueue(self, item):
        if self.IsFullQ():
            print("Queue is full")
            return
        if self.IsEmptyQ():
            self.front = 0
        self.rear = (self.rear + 1) % self.MAX_QUEUE_SIZE
        self.queue[self.rear] = item

    def Dequeue(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX_QUEUE_SIZE

    def peek(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        return self.queue[self.front]

    def Show(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        print("Queue items:")
        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.MAX_QUEUE_SIZE

    def ReverseQueue(self):
        if self.IsEmptyQ():
            print("Queue is empty")
            return
        
        rq = CircularQueue()
        a = []
        f = self.front
        while True:
            a.append(self.queue[f])
            if f == self.rear:
                break
            f = (f+1)% self.MAX_QUEUE_SIZE

        for i in reversed(a):
            rq.Enqueue(i)

        return rq
        

def main():
    my_queue = CircularQueue()
    my_queue.Enqueue(1)
    my_queue.Enqueue(2)
    my_queue.Enqueue(3)
    my_queue.Enqueue(4)
    my_queue.Enqueue(5)
    my_queue.Show()
    my_queue.Dequeue()
    my_queue.Show()
    rq = CircularQueue()
    rq = my_queue.ReverseQueue()
    rq.Show()

if __name__ == "__main__":
    main()
