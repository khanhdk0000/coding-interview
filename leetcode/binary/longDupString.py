class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Use a large Mersenne prime to minimise hash collisions
        MOD = (1 << 61) - 1
        BASE = 131  # prime > 128, covers all ASCII

        n = len(s)
        nums = [ord(c) for c in s]

        def rabin_karp(k: int) -> str:
            """Return any duplicate substring of length k, or '' if none exists."""
            if k == 0:
                return ""

            # Precompute BASE^(k-1) mod MOD — needed to drop the leftmost char
            power = pow(BASE, k - 1, MOD)

            # Compute hash of the first window s[0:k]
            h = 0
            for i in range(k):
                h = (h * BASE + nums[i]) % MOD

            # seen maps hash → starting index of the substring that produced it
            seen = {h: 0}

            for i in range(1, n - k + 1):
                # Roll the hash: remove s[i-1], add s[i+k-1]
                h = (h - nums[i - 1] * power) % MOD
                h = (h * BASE + nums[i + k - 1]) % MOD

                if h in seen:
                    # Hash match — verify to rule out false positives
                    j = seen[h]
                    if s[j : j + k] == s[i : i + k]:
                        return s[i : i + k]
                    # Collision: keep the earlier entry (arbitrary choice; both are valid)
                else:
                    seen[h] = i

            return ""

        # Binary search on the length of the duplicate substring
        lo, hi = 1, n - 1
        result = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            candidate = rabin_karp(mid)

            if candidate:
                result = candidate  # found one — try longer
                lo = mid + 1
            else:
                hi = mid - 1  # too long — try shorter

        return result
