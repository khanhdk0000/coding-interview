from typing import List
import math

# LeetCode 3655 — XOR After Range Multiplication Queries II
#
# For each query [l, r, k, v]:
#   starting at idx=l, while idx <= r: nums[idx] = (nums[idx] * v) % MOD, idx += k
# Return XOR of all elements after all queries.
#
# ─────────────────────────────────────────────────────────────────────────────
# Naive brute force: O(q * n/k) → TLE when k=1, n=q=1e5
# ─────────────────────────────────────────────────────────────────────────────
#
# Optimized: √n decomposition
#   Let B = floor(√n)
#
#   LARGE k (k > B):
#     Each query touches at most n/k < B elements → apply directly, still O(B) per query
#     Total: O(q * B) = O(q * √n)
#
#   SMALL k (k ≤ B):
#     For a fixed k, all elements at positions {l, l+k, l+2k, ...} with the same
#     (l mod k) form an arithmetic sequence of length ceil(n/k).
#     Instead of multiplying each element immediately, record the multiplier in a
#     diff array `mul[k][offset]` over that sequence's indices.
#
#     diff[k][offset] is an array of length ceil(n/k)+1:
#       mul[k][offset][s] *= v  means "multiply by v starting at sequence index s"
#       mul[k][offset][e] stores the "undo" (mod inverse) is NOT needed here —
#       we use prefix products: accumulate left→right, reset at the end marker.
#
#     At the end, one sweep applies all lazy multipliers to nums in O(n * B / k) total
#     which sums to O(n * B * H(B)) ≈ O(n√n log√n) — acceptable.
#
# Overall Time  : O((n + q) * √n)
# Overall Space : O(n * √n)  — the diff arrays

MOD = 10**9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        B = max(1, int(math.isqrt(n)))  # block size = floor(√n)

        # mul[k][offset] is a diff array over the arithmetic sequence
        # with step k and starting remainder offset = (position mod k).
        # Length = ceil(n / k) + 1 slots (the +1 is the sentinel reset slot).
        # mul[k][offset][s] = accumulated multiplier to apply AT sequence index s.
        # We use a dict of lists to avoid allocating for unused (k, offset) pairs.
        from collections import defaultdict

        # mul[k] -> list of length ceil(n/k)+1 for each offset 0..k-1
        # Initialise lazily below.

        # Pre-allocate diff arrays for all small k values
        # mul[k][seq_index] = multiplier factor (product of all v's that start here)
        # We store one flat array per (k, offset) pair.
        mul = {}  # (k, offset) -> list of length (seq_len + 1), init all 1

        def get_seq_len(k, offset):
            # number of elements in nums with index ≡ offset (mod k)
            return (n - offset + k - 1) // k

        for l, r, k, v in queries:
            if k > B:
                # ── LARGE k: apply directly ──────────────────────────────────
                idx = l
                while idx <= r:
                    nums[idx] = nums[idx] * v % MOD
                    idx += k
            else:
                # ── SMALL k: record in diff array ────────────────────────────
                offset = l % k  # which arithmetic sequence does l belong to
                # sequence index of l within its sequence:  l = offset + seq_l * k
                seq_l = (l - offset) // k
                seq_r = (r - offset) // k  # last seq index ≤ r with same offset
                # (r itself may not be ≡ offset mod k,
                #  but we only care about positions ≡ offset)
                # recalculate: positions in [l,r] with step k and starting at l
                # are: l, l+k, l+2k, ... these all share offset = l % k
                # their sequence indices are seq_l, seq_l+1, ..., up to floor((r-offset)/k)
                seq_r = (r - offset) // k

                key = (k, offset)
                if key not in mul:
                    seq_len = get_seq_len(k, offset)
                    mul[key] = [1] * (seq_len + 1)

                arr = mul[key]
                arr[seq_l] = arr[seq_l] * v % MOD  # start multiplying at seq_l
                # To "stop" at seq_r, we'd normally divide — but division mod prime
                # requires modular inverse. Instead store the inverse at seq_r+1:
                # inv(v) mod MOD = pow(v, MOD-2, MOD)  (Fermat's little theorem)
                arr[seq_r + 1] = arr[seq_r + 1] * pow(v, MOD - 2, MOD) % MOD

        # ── Final sweep: apply all small-k lazy multipliers to nums ──────────
        for (k, offset), arr in mul.items():
            running = 1
            seq_idx = 0
            pos = offset  # actual index in nums
            while pos < n:
                running = running * arr[seq_idx] % MOD
                nums[pos] = nums[pos] * running % MOD
                pos += k
                seq_idx += 1

        # ── XOR all elements ─────────────────────────────────────────────────
        res = 0
        for num in nums:
            res ^= num
        return res
