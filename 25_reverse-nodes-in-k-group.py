
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 思路：10min
        # 双指针遍历，时间复杂度是遍历O(n)+翻转O（n）=2O(n),空间复杂度是O(n)
        # 纠正，时间复杂度为 O(n*k) ,head指针会在O(n/k)个节点停留，每次停留进行一次O(k)的翻转。最好的情况为 O(n) 最差的情况未 O(n^2) ，空间复杂度为 O(1) 只需要建立常数的指针变量
        # start指向开始节点，end指向第K个节点，end指针不断向前遍历，直到第K个节点。
        # 翻转start->end区间的链表
        # start=end,end指针继续向前遍历下一循环，如果end指针遍历的节点数量不足K个，则不翻转
        # 错误点！：翻转后的head会改变，第一段翻转的end节点是新的head
        # 错误点！：翻转完成后，需要续接左右两段链表。preNode指向翻转后的开始节点(已变为end),翻转后的结束节点(已变为start)指向nextNode
        # 错误点！：链表翻转不熟练，没用双指针
        # 错误点2：尾部刚好为K个要继续reverse
        # 错误点3：退出条件要用节点判断，不能用节点的值判断，可能不同节点有重复val
        # coding 1hour
        # 边界
        if k == 1:
            return head
        # 初始化
        start = end = head
        num = 1
        newHead = preNode = None
        # 外循环遍历整个链表
        while start:
            #内循环每次遍历K个节点
            while num < k and end.next:
                end = end.next
                num += 1
            # 尾部不足K个跳出
            # 错误点2：尾部刚好为K个要继续reverse
            if not end.next and num != k:
                break
            # 错误点！：翻转后的head会改变，第一段翻转的end节点是新的head
            if not newHead:
                newHead = end
            # 先缓存nextNode，翻转后会丢失
            nextNode = end.next
            # 翻转区间从start节点开始到end节点结束
            self.reverseListNode(start,end)
            # 翻转后start变成end,end变成start
            # 错误点！：翻转完成后，需要续接左右两段链表。preNode指向翻转后的开始节点(已变为end),翻转后的结束节点(已变为start)指向nextNode
            start.next = nextNode
            if preNode:
                preNode.next = end
            # 初始化下一区间的数据,start从下一段的第一个节点开始
            preNode = start
            start = end = nextNode
            print('next')
            print(newHead)
            num = 1
            # print(num,k)
        return newHead
    
    def reverseListNode(self,start,end):
        # 双指针翻转法
        # pre指针是节点翻转后指向的节点，翻转第一个节点时，pre是None,翻转其他节点时，pre是上一个节点，
        # 每次只翻转一个节点：
        # 1先用一个中间变量缓存下一个节点，
        # 2翻转节点的
        # 3pre,cur指针分别向前移一位
        print('before')
        pre,cur = start,start.next
        print(pre.val,cur.val,end.val)
        # 错误点3：退出条件要用节点判断，不能用节点的值判断，可能不同节点有重复val
        while pre != end:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # print('after')
        # print(pre.val,cur.val,end.val)

# 犯错的用例 
# 尾部刚好-》错误点2
#[1,2]
#2
# 有重复val-》错误点3
#[1,7,3,2,7,0,1,0,0]
#4