'''
在 Python 程序中，我们把单个或多个字符用单引号或者双引号包围起来，
就可以表示一个字符串。字符串中的字符可以是特殊符号、英文字母、中文字符、
日文的平假名或片假名、希腊字母、Emoji 字符（如：💩、🐷、🀄️）等。
'''
s1 = 'hello, world!'
s2 = '你好，世界！'
s3 = '''hello,
world!'''
print(s1)
print(s2)
print(s3)

# 转义字符
s4 = '\'hello,world!\''
s5 = '\\hello,world!\\'
print(s4)
print(s5)

# 原始字符串
s6 = r'\'hello,world!\''
s7 = r'\\hello,world!\\'
print(s6)
print(s7)

# 字符串的运算
# 1.拼接和重复
s1 = 'hello' + ', ' + 'world' + '!'
print(s1)
s2 = 'hello' * 3
print(s2)

# 2.比较运算
s3 = 'apple'
s4 = 'banana'
print(s3 == s4)
print(s3 != s4)
print(s3 < s4)

# 3.成员运算
s5 = 'hello, world!'
s6 = 'world'
print(s6 in s5)
print('Python' not in s5) 

# 4.字符串长度
s7 = 'hello, world!'
print(len(s7))

# 5.索引和切片
s8 = 'hello, world!'
print(s8[0])      # 第一个字符
print(s8[-1])     # 最后一个字符
print(s8[0:5])    # 前五个字符
print(s8[7:])     # 从第八个字符到结尾
print(s8[:5])     # 从开头到第五个字符

# 6.字符遍历
s9 = 'hello'
for char in s9:
    print(char)

for index in range(len(s9)):
    print(s9[index])

# 7.字符串常用方法
s10 = '  Hello, World!  '
print(s10.lower())        # 转小写
print(s10.upper())        # 转大写
print(s10.strip())       # 去除首尾空白