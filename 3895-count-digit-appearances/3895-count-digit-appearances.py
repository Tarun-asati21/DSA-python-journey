class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        def count(num, dig) :
            temp = str(num)
            check = str(dig)
            count = 0
            for ch in  temp :
                if ch == check :
                    count += 1
            return count
        
        final = 0
        for num in nums :
            final += count(num, digit)
        return final