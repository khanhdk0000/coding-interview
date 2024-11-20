class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import defaultdict

        n = len(s)
        total_counts = {'a': 0, 'b': 0, 'c': 0}

        # Count total occurrences of each character
        for char in s:
            total_counts[char] += 1

        # Check if it's possible to have at least k of each character
        if any(total_counts[char] < k for char in 'abc'):
            return -1

        # If k is 0, no need to take any characters
        if k == 0:
            return 0

        max_window_size = 0
        window_counts = {'a': 0, 'b': 0, 'c': 0}
        left = 0

        for right in range(n):
            # Add the current character to the window
            window_counts[s[right]] += 1

            # Shrink the window from the left if counts exceed allowable removals
            while any(window_counts[char] > total_counts[char] - k for char in 'abc'):
                window_counts[s[left]] -= 1
                left += 1

            # Update maximum window size
            max_window_size = max(max_window_size, right - left + 1)

        # Minimum minutes needed is total length minus max window size
        return n - max_window_size

sol = Solution()
print(sol.takeCharacters("aabaaaacaabc", 2)) 
print(sol.takeCharacters("a", 1)) 
        