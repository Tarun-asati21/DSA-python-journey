class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # In standard Binary Search, when target is not found, the left pointer ends up pointing to the exact index where target should be inserted.
        start=0
        end = len(nums)-1
        while start <= end :
            mid = (start+end) //2
            if nums[mid] == target :
                return mid 
            elif nums[mid] < target :
                start = mid+1
            else :
                end = mid-1
        return start