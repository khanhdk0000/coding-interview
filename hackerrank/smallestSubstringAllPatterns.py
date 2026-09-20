from heapq import heappush, heappop
from typing import List


def findSmallestSubstringWindow(patterns: List[str], S: str) -> List[int]:
    """Smallest window [l, r] of S containing an occurrence of every pattern.

    Sweep occurrence end indices left to right. All occurrences of one pattern
    share a length, so the last one ending at or before r also has the largest
    start -- so for a fixed r the best left edge is min(best_start[pid]).
    Lazy heap keeps that min while the per-pattern starts only grow.
    """
    pats = list(set(patterns))  # duplicates are the same constraint
    events = []
    for pid, p in enumerate(pats):
        i = S.find(p)
        if i < 0:
            return [-1, -1]
        # ponytail: str.find loop is C-speed; Aho-Corasick only if this TLEs
        while i >= 0:
            events.append((i + len(p) - 1, i, pid))
            i = S.find(p, i + 1)
    events.sort()

    best_start = {}
    heap = []
    ansL = ansR = -1
    for end, start, pid in events:
        best_start[pid] = start
        heappush(heap, (start, pid))
        if len(best_start) == len(pats):
            while heap[0][0] != best_start[heap[0][1]]:
                heappop(heap)  # stale entry
            left = heap[0][0]
            if ansL < 0 or end - left < ansR - ansL:
                ansL, ansR = left, end
    return [ansL, ansR]


if __name__ == "__main__":
    assert findSmallestSubstringWindow(["abc", "zyx"], "xyzabcabczyx") == [6, 11]
    assert findSmallestSubstringWindow(["a"], "a") == [0, 0]
    assert findSmallestSubstringWindow(["b"], "a") == [-1, -1]
    assert findSmallestSubstringWindow(["a", "a"], "xa") == [1, 1]  # duplicate patterns
    assert findSmallestSubstringWindow(["aa", "a"], "baa") == [1, 2]  # overlapping
    assert findSmallestSubstringWindow(["ab", "b"], "ab") == [0, 1]  # nested
    print("ok")
