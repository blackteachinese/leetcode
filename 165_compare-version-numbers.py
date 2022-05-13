class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def stripPre0(c:str)->int:
            # 最后一位如果是0，保留不过滤
            i=0
            while i < len(c) - 1:
                if c[i] != '0':
                    break
                i += 1
            return int(c[i:])
        # 1.用.将字符串分割为数组
        list1=version1.split('.')
        list2=version2.split('.')
        # 2.从左到右逐个比较数组元素，比较先strip掉前面的0
        i=0
        while i < len(list1) or i < len(list2):
            subV1=stripPre0(list1[i]) if i < len(list1) else 0
            subV2=stripPre0(list2[i]) if i < len(list2) else 0
            if subV1 > subV2:
                return 1
            elif subV1 < subV2:
                return -1
            i+=1
        return 0
        # 3.只要某一位大，则判断结束
        # 4.判断到最后如果还是相等，此时数组个数不一致，判断剩余元素是否全是0，如果是则相等，否则该数组对应的版本号更大

print(Solution().compareVersion("1.01","1.001"))
print(Solution().compareVersion("1.0","1.0.0"))
print(Solution().compareVersion("0.1","1.1"))