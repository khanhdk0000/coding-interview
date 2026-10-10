from typing import List


def countBribes(q: List[int]):
    bribes = 0
    for i, p in enumerate(q):
        # p started at index p-1; moving forward more than 2 spots = 3+ bribes
        if p - 1 - i > 2:
            return "Too chaotic"
        # Anyone who bribed p ends up ahead of p, and can't get further
        # forward than index p-2 (a briber x > p starts at index x-1 >= p,
        # then moves forward at most 2), so only scan from there.
        for j in range(max(0, p - 2), i):
            if q[j] > p:
                bribes += 1
    return bribes


def minimumBribes(q: List[int]) -> None:
    print(countBribes(q))


if __name__ == '__main__':
    assert countBribes([2, 1, 5, 3, 4]) == 3
    assert countBribes([2, 5, 1, 3, 4]) == "Too chaotic"
    assert countBribes([1, 2, 5, 3, 7, 8, 6, 4]) == 7
    assert countBribes([5, 1, 2, 3, 7, 8, 6, 4]) == "Too chaotic"
    assert countBribes([1, 2, 3, 5, 4, 6, 7, 8]) == 1
    assert countBribes([4, 1, 2, 3]) == "Too chaotic"

    # random valid queues: answer = number of inversions (each bribe is one adjacent swap)
    import random
    rng = random.Random(0)
    for _ in range(500):
        n = rng.randint(1, 10)
        q = list(range(1, n + 1))
        for _ in range(rng.randint(0, 15)):
            k = rng.randint(1, n - 1) if n > 1 else 0
            if k:
                q[k - 1], q[k] = q[k], q[k - 1]
        inv = sum(q[a] > q[b] for a in range(n) for b in range(a + 1, n))
        chaotic = any(p - 1 - i > 2 for i, p in enumerate(q))
        assert countBribes(q) == ("Too chaotic" if chaotic else inv), q
    print("ok")
