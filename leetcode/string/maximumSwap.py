class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        uniqueDigits = set(digits)
        sortedDigits = sorted(uniqueDigits, reverse=True)
        digitRankMap = {digit: rank for rank, digit in enumerate(sortedDigits)}
        digitCountMap = {}
        for digit in digits:
            if digit not in digitCountMap:
                digitCountMap[digit] = 0
            digitCountMap[digit] += 1
        currentRank = 0
        print(digits)
        for index, digit in enumerate(digits):
            if index > 0 and digit != digits[index - 1]:
                currentRank += 1
            print(digitRankMap[digit], currentRank)
            if digitRankMap[digit] > currentRank or (digitRankMap[digit] == currentRank and digitCountMap[digit] > 1):
                # Find remaining max digit
                maxDigit = max((d for d in digits[index + 1:]))
                maxDigitIndexFromEnd = index
                print("aaaa",maxDigit, maxDigitIndexFromEnd)
                for i in range(len(digits) - 1, index, -1):
                    if digits[i] == maxDigit:
                        maxDigitIndexFromEnd = i
                        break
                digits[index], digits[maxDigitIndexFromEnd] = digits[maxDigitIndexFromEnd], digits[index]
                break
            digitCountMap[digit] -= 1
        return int("".join(map(str, digits)))

sol = Solution()
# print(sol.maximumSwap(98368)) # 7236
# print(sol.maximumSwap(2736)) # 7236
# print(sol.maximumSwap(9973)) # 7236
# print(sol.maximumSwap(1993)) # 7236
print(sol.maximumSwap(545)) # 7236