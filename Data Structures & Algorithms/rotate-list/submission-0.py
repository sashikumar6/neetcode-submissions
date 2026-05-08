# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        curr=head
        n=1
        while curr.next:
            curr=curr.next
            n+=1
        k=k%n
        move=n-k

        if k == 0:
            return head

        tail_new=head
        curr.next=head

        while move-1>0:
            tail_new=tail_new.next
            move-=1

        new_head = tail_new.next
        tail_new.next=None
        

        return new_head
