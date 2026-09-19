class MyCircularQueue:
    """LeetCode 622 - fixed-size queue on a ring buffer.

    head is the index of the front element; tail is derived as
    (head + count) % k, so freed slots in front get reused.
    """

    def __init__(self, k: int):
        self.buf = [0] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buf[(self.head + self.count) % len(self.buf)] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.buf)
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.buf[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[(self.head + self.count - 1) % len(self.buf)]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.buf)


def demo():
    q = MyCircularQueue(3)
    assert q.isEmpty() and q.Front() == -1 and q.Rear() == -1
    assert q.enQueue(1) and q.enQueue(2) and q.enQueue(3)
    assert not q.enQueue(4)  # full
    assert q.Rear() == 3 and q.Front() == 1
    assert q.isFull()
    assert q.deQueue()          # frees slot 0
    assert q.enQueue(4)         # wraps around into it
    assert q.Front() == 2 and q.Rear() == 4
    assert q.deQueue() and q.deQueue() and q.deQueue()
    assert q.isEmpty() and not q.deQueue()
    print("ok")


if __name__ == "__main__":
    demo()
