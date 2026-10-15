# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next or not head.next.next:
            return head
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None

        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        

        back = prev
        front = head

        while back:
            front_next = front.next
            back_next = back.next

            front.next = back
            back.next = front_next
            front = front_next
            back = back_next
        
        return head

        


        