class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for num in range(num1, num2 + 1):
            temp = str(num)
            if len(temp) < 3:
                continue
                
            for j in range(1, len(temp) - 1):
                prev_digit = int(temp[j - 1])
                curr_digit = int(temp[j])
                next_digit = int(temp[j + 1])
                
                # Check for Peak
                if prev_digit < curr_digit > next_digit:
                    waviness += 1
                # Check for Valley
                elif prev_digit > curr_digit < next_digit:
                    waviness += 1
                    
        return waviness

