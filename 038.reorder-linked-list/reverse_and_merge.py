# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second_half = slow.next
        reversed_second_half = slow.next = None
        while second_half:
            temp = second_half.next
            second_half.next = reversed_second_half
            reversed_second_half = second_half
            second_half = temp

        # Merge the two
        first_half, second_half = head, reversed_second_half
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2