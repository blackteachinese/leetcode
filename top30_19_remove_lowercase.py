import re


def main(string):
    # return re.sub(re.compile(r'[^a-z]'),'',string)
    # [^...], 匹配不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
    return re.sub(r'[^a-z]','',string)


string='Testing@'
rs = main(string)
print(rs)