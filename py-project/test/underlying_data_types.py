# 基础数据类型
"""
int：整数
float：浮点数
bool：布尔值
str：字符串
list：
tuple：
set：
dict：
bytes：
运算符：
文件操作：
"""

print(10/3) # 小数：数据范围是无限的，整数：在某一个特定的区间内是可以表示的很清楚的。
# 0~1
# 计算机是一个二进制的产品：0，1
# 计算机表示一个小数是会有误差的

# bool：用来做条件判断的
#   取值范围：True, False
# 基础数据类型之间的转化：
#                       所有非零的数字为True, 0为False
#                       所有非空的字符串为True,空字符串为False

# while 1:
#     content = input('输入要说的话：')
#     if content:
#         print('这就是我要说的话：', content)
#     else:
#         break


# # 1.字符串的格式化问题
# # 我叫XXX，我住在XXX，我今年XXX岁，我喜欢做XXX。
# name = input("请输入姓名：")
# address = input("请输入地址：")
# age = int(input("请输入年龄："))
# hobby = input("请输入爱好：")
#
# # %s(字符串占位) %d(整数占位) %f(小数占位)
# s = "我叫%s，我住在%s，我今年%d岁，我喜欢做%s。" % (name, address, age, hobby)
# s0 = "我叫%s。" % name
# s1 = "我叫{}，我住在{}，我今年{}岁，我喜欢做{}。".format(name, address, age, hobby)
# s2 = f"我叫{name}，我住在{address}，我今年{age}岁，我喜欢做{hobby}。"
# print(s)
# print(s0)
# print(s1)
# print(s2)

# # 2.索引和切片
# # (1)索引，按照位置提取元素
# q = '我是二大爷'
# # 可以采用索引的方式来提取某一个字符
# print(q[3])
# print(q[-1])

# # (2)切片：从一个字符串中提取一部分内容
# w = '我是你二大爷啊，侄孙子，你还记得我吗？'
# print(w[14:16])  # 从索引14开始进行切片，到索引16前结束，切片拿不到第二个位置的元素
# # 语法：w[start:end] 从start到end进行切片，但是取不到end,[start, end)
# print(w[0:7])
# print(w[:7])  # 如果start是从头开始切片，可以省略
# print(w[8:])  # 如果end是结尾，可以省略
# print(w[:])  # 从头到结尾
# print(w[-5:-3])  # 倒数切片

# # (3)字符串的常规操作
# # 字符串的操作一般不会对原字符串产生影响，一般是返回一个新字符串
# #         1.字符串大小写转换
# r = 'python yes!'
# print(r.capitalize(), '第一个单词的首字母大写')  # 第一个单词的首字母大写
#
# r1 = 'I have how money'
# print(r1.title(), '每个单词的首字母大写')  # 每个单词的首字母大写
#
# r2 = 'I HAVE HOW MONEY'
# print(r2.lower(), '大写转小写')  # 大写转小写
#
# r3 = 'i have how noney'
# print(r3.upper(), '小写转大写')  # 小写转大写
#
# # 大小写转换，常用在验证码转化校验

# (4)字符串的切割和替换
# strip() 去除字符串左右两端的空白符（空格， \t, \n）
r4 = '   这段字符串   有  好多  空格！    '
print(r4.strip())

# replace(old, new) 字符串替换
r5 = '   这段字符串   拿来  替换  空格的喔！    '
print(r5.replace(' ', ''))