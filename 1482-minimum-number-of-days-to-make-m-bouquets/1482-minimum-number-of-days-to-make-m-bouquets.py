class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def possible(arr, day, m ,k):
            count=0
            bouqets =0
            for i in range (0, len(arr)):
                if arr[i] <=  day :
                    count+=1
                else :
                    bouqets += count//k
                    count=0
            bouqets += count//k  # in case of last counter
            return bouqets >= m 

        if len(bloomDay) < m*k:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high :
            mid= (low+high)//2
            if possible(bloomDay, mid, m, k) == True :
                high=mid-1
            else :
                low = mid+1
        return low