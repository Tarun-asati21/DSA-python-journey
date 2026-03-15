class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        def oper(arr):
            temp =[]
            for i in range(1, len(arr)):
                sumi = arr[i]+arr[i-1]
                temp.append(sumi)
            mini = min(temp)

            a=0
            b=0
            for j in range(0, len(temp)):
                if temp[j] == mini  :
                    a = j
                    b= j+1
                    break
            
            arr[a]=mini
            del arr[b]
            return arr
        
        if nums == sorted(nums) :
            return 0
        else :
            count = 0
            for i in range(0, len(nums)):
                new_arr = oper(nums)
                count += 1
                if new_arr == sorted(new_arr) :
                    return count
