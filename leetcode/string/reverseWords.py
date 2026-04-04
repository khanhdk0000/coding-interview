class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire string
        reverse(chars, 0, n - 1)

        # Step 2: Walk through, find each word, write it back,
        i, j = 0, 0
        last_index = 0  # tracks end of the last written word

        while j < n:
            # Skip spaces before the word
            while j < n and chars[j] == " ":
                j += 1

            start_index = i  # remember where this word starts

            # Copy word characters into position i
            while j < n and chars[j] != " ":
                chars[i] = chars[j]
                i += 1
                j += 1
                last_index = i  # update end of last valid word

            # Reverse the word we just wrote
            reverse(chars, start_index, last_index - 1)

            if j < n:
                chars[i] = " "
                i += 1

        return "".join(chars[:last_index])
