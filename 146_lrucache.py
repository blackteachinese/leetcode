from collections import defaultdict
from email.policy import default


class DLinkNode: # 自定义双向链表
    def __init__(self,key=None,value=None) -> None:
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    # 参考题解
    # 难度在于实现O(1)复杂度
    # 取值肯定要用哈希表
    # 存储数据的使用顺序可以用列表结构，但最好所有操作都是O（1）
    # 需要支持的操作1移除头部数据2尾部插入3将中间某个数据移到尾部
    # ！！！！！list实现操作3不能达到O1
    # 如果用单链表，操作3的时间复杂度是O（n）
    # 使用双链表时，操作3可以达到O（n）
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        # ！！！！！重要错误点：一开始没有创建空的head和tail指针，导致指针前后关系处理很复杂，有些case容易出错
        self.headNode = DLinkNode()
        self.tailNode = DLinkNode()
        self.headNode.next = self.tailNode
        self.tailNode.pre = self.headNode
        self.size = 0

    def get(self, key: int) -> int:
        # print('get: key:',key,self.dic)
        # 错误点：取出的值，忘记要放到最后
        if key in self.dic:
            self.move2end(key)
            return self.dic[key].value
        else:
            return -1

    def move2end(self,key) -> None:
        node = self.dic[key]
        # 从原位置取出node，补上空缺
        node.pre.next = node.next
        node.next.pre = node.pre
        #插到到尾部
        self.tailNode.pre.next = node
        node.pre = self.tailNode.pre
        node.next = self.tailNode
        self.tailNode.pre = node


    def put(self, key: int, value: int) -> None:
        # print('push: key:',key,'value:',value,self.dic)
        if key in self.dic: # 要插入的值已存在，移到最后
            node = self.dic[key]
            node.value = value # 更新元素
            self.move2end(key)
        else: 
            #如果未存在，先添加新元素到最后
            nextNode = DLinkNode(key,value)
            self.tailNode.pre.next = nextNode
            nextNode.pre = self.tailNode.pre
            nextNode.next = self.tailNode
            self.tailNode.pre = nextNode
            self.dic[key] = nextNode
            # 如果超过size,移出第一个元素
            if len(self.dic) > self.capacity:
                # 需要O(1)速度到pop掉头部元素

                del self.dic[self.headNode.next.key]
                self.headNode.next = self.headNode.next.next
                self.headNode.next.pre = self.headNode