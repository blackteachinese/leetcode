# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 外循环，指针a遍历链表1，指针b遍历链表2
        # 当a.next.val >= b.next.val,将b指向的节点插入a和a.next之间.
        # a向前移一个节点，b也向前移一个节点
        # 继续循环判断b和a.next的关系，直到当b.val > a.val时，a指针向前移动
        # 退出条件a = None and b = None
        # 边界值处理
        # 头部处理
        # 尾部，如果a先遍历完，b剩余节点全部插到a后面，如果b先遍历完，直接结束。
        
        # 边界值处理
        if not list1 or not list2:
            return list1 if list1 else list2
        prea,a,b = None,list1,list2
        newList = a if a.val < b.val else b # 记录新的头
        while True:
            while b.val <= a.val:
                # 插入
                nextb  = b.next
                # 头部处理，如果
                if prea:
                    prea.next = b
                b.next = a
                # 向右遍历1位
                prea = b
                print(newList)
                # 如果b链表先遍历完，结束
                if not nextb:
                    # 这里要直接return，用break会死循环
                    return newList
                b = nextb
            # 如果a链表先遍历完，需要拼接剩余的b链表拼接到a的尾结点后面
            if a.next:
                prea = a
                a = a.next
            else:
                a.next = b
                return newList

class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代，题解思路
        # 边界值处理
        if not list1 or not list2:
            return list1 if list1 else list2
        # a,b可以省略掉
        newhead,a,b = ListNode(),list1,list2
        # prea用来穿节点，它永远指向已经穿好的下个节点
        prea = newhead
        while a and b:
            if a.val < b.val:
                # 如果a小，prea就穿a
                prea.next = a
                a = a.next
            else :
                # 如果b小，prea就穿b
                prea.next = b
                b = b.next
            # 穿好后pre要向前移一位
            prea = prea.next # 错误点!!:漏掉这一步，最后只剩一个节点
        prea.next = a if a is not None else b #穿上最后剩下的一段
        return newhead.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归，题解思路
        # 边界值处理
        if not list1 or not list2:
            return list1 if list1 else list2
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
        return list1 if list1.val < list2.val else list2