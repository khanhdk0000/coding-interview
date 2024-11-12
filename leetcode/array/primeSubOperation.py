from typing import List
class Solution:
    def getPrime(self, primes, low, high):
        for prime in primes:
            if low <= prime < high:
                return prime
        return high

    def primeSubOperation(self, nums: List[int]) -> bool:
        # use sieve of eratosthenes to get all prime numbers
        max_num = max(nums) + 1
        is_prime = [True] * (max_num)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num, i):
                    is_prime[j] = False
        primes = [i for i, val in enumerate(is_prime) if val]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                low = nums[i] - (nums[i + 1] - 1)
                high = nums[i]
                prime = self.getPrime(primes, low, high)
                if prime == high:
                    return False
                else:
                    nums[i] -= prime
        return True


sol = Solution()
print(sol.primeSubOperation([4,9,6,10])) # True
print(sol.primeSubOperation([5,8,3])) # True

