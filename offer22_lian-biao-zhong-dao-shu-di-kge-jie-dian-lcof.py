# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #方法1:双指针法，两个指针相差k位，一个到尾部，另一个就到倒数第K个节点
        # time:O(n),n is the count of link
        # border
        if not head :return head
        # logic
        l=r=head
        # r run k node
        for i in range(0,k-1):
            r=r.next
        # r run until None
        while r:
            if r.next == None:
                break
            l = l.next
            r = r.next
           
        return l

    