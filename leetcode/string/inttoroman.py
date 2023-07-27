
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""


from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        unit = 1
        while num > 0:
            subStract = num % (10**unit)
            num -= subStract
            # print(subStract, unit, num)

            if unit == 1:
                if subStract == 1:
                    roman.append("I")
                    unit += 1
                    continue
                elif subStract == 5:
                    roman.append("V")
                    unit += 1
                    continue
                elif subStract == 9:
                    roman.append("IX")
                    unit += 1
                    continue
                elif subStract == 4:
                    roman.append("IV")
                    unit += 1
                    continue
                elif 5 < subStract < 9:
                    numOfOne = subStract - 5
                    roman.append("V" + "I"*numOfOne)
                    unit += 1
                    continue
                elif subStract < 5:
                    roman.append("I"*subStract)
                    unit += 1
                    continue
            elif unit == 2:
                if subStract == 10:
                    roman.append("X")
                    unit += 1
                    continue
                elif subStract == 40:
                    roman.append("XL")
                    unit += 1
                    continue
                elif subStract == 50:
                    roman.append("L")
                    unit += 1
                    continue
                elif subStract == 90:
                    roman.append("XC")
                    unit += 1
                    continue
                elif 50 < subStract < 90:
                    numOfTen = subStract - 50
                    numOfTen = numOfTen // 10 
                    roman.append("L" + "X"*numOfTen)
                    unit += 1
                    continue
                elif subStract < 50:
                    numOfTen = subStract // 10
                    roman.append("X"*numOfTen)
                    unit += 1
                    continue
            elif unit == 3:
                if subStract == 100:
                    roman.append("C")
                    unit += 1
                    continue
                elif subStract == 400:
                    roman.append("CD")
                    unit += 1
                    continue
                elif subStract == 500:
                    roman.append("D")
                    unit += 1
                    continue
                elif subStract == 900:
                    roman.append("CM")
                    unit += 1
                    continue
                elif 500 < subStract < 900:
                    numOfHundred = subStract - 500
                    numOfHundred = numOfHundred // 100
                    roman.append("D" + "C"*numOfHundred)
                    unit += 1
                    continue
                elif subStract < 500:
                    numOfHundred = subStract // 100
                    roman.append("C"*numOfHundred)
                    unit += 1
                    continue
            else:
                numOfThousand = subStract // 1000
                roman.append("M"*numOfThousand)
        return "".join(roman[::-1])
    
"""
Better solution:
class Solution {
public:
    string intToRoman(int num) {
        string ones[] = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
        string tens[] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string hrns[] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string ths[]={"","M","MM","MMM"};
        
        return ths[num/1000] + hrns[(num%1000)/100] + tens[(num%100)/10] + ones[num%10];
    }
};
"""

input = 3
input = 58
input = 1994


sol = Solution()

print(sol.intToRoman(input))