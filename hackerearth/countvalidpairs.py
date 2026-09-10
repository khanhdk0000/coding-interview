def solve(N, nums):
    # Digit sum is the only thing that matters, so bucket by it and count
    # pairs inside each bucket. nums[i] <= 1e9 => digit sum <= 81 (999999999).
    counts = [0] * 82
    for x in nums:
        counts[sum(map(int, str(x)))] += 1
    # A bucket of size c contributes C(c, 2) = c*(c-1)/2 pairs with i < j.
    return sum(c * (c - 1) // 2 for c in counts)


N = int(input())
nums = list(map(int, input().split()))

out_ = solve(N, nums)
print(out_)
