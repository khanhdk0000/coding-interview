from collections import deque


class MyStack:
    """LeetCode 225 - stack backed by a single queue.

    push rotates the queue so the new element sits at the front;
    pop/top then read the front like a normal queue.
    """

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # rotate the older elements behind x -> O(n) push, O(1) pop/top
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


def demo():
    s = MyStack()
    assert s.empty()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert s.top() == 1
    assert not s.empty()
    assert s.pop() == 1
    assert s.empty()
    print("ok")


if __name__ == "__main__":
    demo()
