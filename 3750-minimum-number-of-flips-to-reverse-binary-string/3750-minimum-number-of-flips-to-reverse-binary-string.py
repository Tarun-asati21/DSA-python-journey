class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = bin(n)[2:]
        reverse = binary[::-1]
        count=0
        for i in range(len(binary)):
            if int(binary[i]) != int(reverse[i]) :
                count+=1
        return count
