class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        arr=[0,1,1]
        while arr[-1] < n//2 :
            temp = arr[-1]+arr[-2]
            arr.append(temp)
        print(arr)
        if sum(arr[-3:])==n :
            return True
        return False

        
