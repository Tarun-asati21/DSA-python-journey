class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # brute force
        # t_value = ord(target)
        # for i in range(len(letters)):
        #     value = ord(letters[i])
        #     if value > t_value :
        #         return letters[i]
        # return letters[0]

        # better solution
        if letters[-1] < target :
            return letters[0]

        left, right = 0, len(letters) - 1
        ans = letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                ans = letters[mid]
                right = mid - 1  
            else:
                left = mid + 1
        return ans
            
        