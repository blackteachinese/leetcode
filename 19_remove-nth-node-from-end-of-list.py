# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


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
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 方法：先找到倒数第N个结点的前一个节点，删除第N个节点
        # 边界处理
        if not head :return head
        dump = ListNode(0,head) # 加dump头结点，简化边界逻辑
        preN = self.getKthFromEnd(dump,n+1)
        # print(preN.val)
        if preN and preN.next:
            preN.next = preN.next.next if preN.next.next else None
        return dump.next