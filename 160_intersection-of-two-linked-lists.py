from collections import defaultdict
from pickle import NONE
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 1 遍历判断节点是否同时存在两个链表 O（MN）
        # 2 一个链表用哈希表存储，遍历另一个链表 O（N）
        
        # 边界情况
        if not headA or not headB:
            return NONE
        # 哈希表
        sets = set()
        while headA:
            sets.add(headA)
            headA = headA.next
        # 遍历链表B
        while headB:
            if headB in sets:
                return headB
            headB = headB.next
        return None

        # 3 双指针：
        # 关键：如果两个链表相交，他们必定会有公共尾部
            
