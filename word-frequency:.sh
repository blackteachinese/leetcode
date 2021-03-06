cat words.txt | xargs -n 1 | sort | uniq -c | sort -nr | awk '{print $2" "$1}'

# 拆分单词：xargs 将所有行转为单列，默认会以空格、回车等不可见符号作为分隔符，通过"-d"指定分隔符为"#"。“-n1”的意思是每次获取一个参数。
# sort 比较原则是从首字符向后，依次按ASCII码值进行比较，最后将他们按升序输出。
# 按数字排序：sort -nr 表示依照数值的大小降序排序。
# 统计次数：uniq -c 表示在每列旁边显示该行重复出现的次数。
# awk + print 函数将 1、2 列位置互换