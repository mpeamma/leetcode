class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M")]
        combo_numerals = [(900, "CM"), (400, "CD"), (90, "XC"), (40, "XL"), (9, "IX"), (4, "IV")]
        all_nums = numerals + combo_numerals
        all_nums.sort(key=lambda x: x[0])
        all_nums.reverse()
        
        result = ""
        while num > 0:
            for x in all_nums:
                if num >= x[0]:
                    if x in combo_numerals:
                        num -= x[0]
                        result += x[1]
                    else:
                        rem = num % x[0]
                        count = num // x[0]
                        for _ in range(count): result += x[1]
                        num = rem
        return result

print(Solution().intToRoman(1994))