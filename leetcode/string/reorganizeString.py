import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        """LeetCode 767 - rearrange so no two adjacent chars are equal.

        Max-heap by remaining count. Each round pops the two most common
        chars and emits both: two copies of one char can never be emitted
        back to back, because the round in between always spends a
        different char.
        """
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        # heapq is a min-heap, so store negated counts to pop the largest
        heap = [(-cnt, char) for char, cnt in counts.items()]
        heapq.heapify(heap)

        res = []
        while len(heap) >= 2:
            cnt1, char1 = heapq.heappop(heap)
            cnt2, char2 = heapq.heappop(heap)
            res.append(char1)
            res.append(char2)
            # counts are negative, so += 1 spends one copy
            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1 + 1, char1))
            if cnt2 + 1 < 0:
                heapq.heappush(heap, (cnt2 + 1, char2))

        if heap:
            cnt, char = heap[0]
            # more than one copy left with nothing to separate them
            if -cnt > 1:
                return ""
            # safe: a single leftover is always char1, never the last char emitted
            res.append(char)

        return "".join(res)


def _max_count(s: str) -> int:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return max(counts.values())


def _valid(original: str, out: str) -> bool:
    if sorted(original) != sorted(out):
        return False
    return all(a != b for a, b in zip(out, out[1:]))


def demo():
    sol = Solution()
    assert _valid("aab", sol.reorganizeString("aab"))
    assert sol.reorganizeString("aaab") == ""      # 3 copies, only 4 slots
    assert sol.reorganizeString("a") == "a"
    assert sol.reorganizeString("aa") == ""
    assert _valid("aabb", sol.reorganizeString("aabb"))
    assert _valid("vvvlo", sol.reorganizeString("vvvlo"))   # tight but feasible
    assert _valid("abbabbaaab", sol.reorganizeString("abbabbaaab"))
    # exhaustive small check
    from itertools import product
    for n in range(1, 8):
        for t in product("abc", repeat=n):
            word = "".join(t)
            out = sol.reorganizeString(word)
            feasible = _max_count(word) <= (n + 1) // 2
            assert (out != "") == feasible, word
            if out:
                assert _valid(word, out), word
    print("ok")


if __name__ == "__main__":
    demo()
