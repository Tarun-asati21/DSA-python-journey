# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst=[]
        curr=head
        while curr :
            lst.append(curr.val)
            curr=curr.next
        
        l=0
        r=len(lst)-1
        while l<= r :
            if lst[l]==lst[r]:
                l+=1
                r-=1
            else :
                return False
        return True