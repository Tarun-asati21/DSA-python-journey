class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        temp =[]
        arr.sort()
        for i in range (1, len(arr)):
            diff = arr[i]-arr[i-1]
            temp.append(diff)
        mini =  min(temp)

        ans = []
        for j in range(0, len(temp)):
            if temp[j]==mini :
                ans.append([arr[j],arr[j+1]])
        return ans
