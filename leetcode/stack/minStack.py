class MinStack:
    """LeetCode 155 - stack with O(1) getMin.

    Each entry carries the min of everything at or below it, so popping
    restores the previous min for free.
    """

    def __init__(self):
        self.stack = []  # (value, min at this depth)

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def demo():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
    s.push(-2)
    assert s.getMin() == -2
    s.pop()
    assert s.getMin() == -2
    print("ok")


if __name__ == "__main__":
    demo()
