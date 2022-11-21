# 单行注释
print("随便试一下")
"""
多行注释
"""
'''
多行注释
'''
print("随便试俩下")

# 字符串
val = 'value'
print(val)

# 常量
PI = 3.14
print(PI)

PI = 45625
print(PI)

# 计算
val1 = input('请输入第一个数字:')
val2 = input('请输入第二个数字:')
val1 = int(val1);
val2 = int(val2);
print(val1 + val2)

# if判断一
money1 = 200
if money1 > 50:
    print('我有好多钱')
print('我没有好多钱')

# if判断二
money2 = 200
if money2 > 50:
    print('我有好多钱')
else:
    print('我没有好多钱')

# if判断三
money3 = int(input('请输入拥有多少钱'))
if money3 > 500:
    if money3 > 800:
        print('隆江猪脚饭加猪脚')
    else:
        print('蛋炒饭加蛋')
else:
    print('我没有钱')

# if判断四
money4 = int(input('请输入拥有多少钱'))
if money4 > 5000:
    print('隆江猪脚饭加猪脚')
elif money4 > 3000:
    print('隆江猪脚饭')
elif money4 > 1000:
    print('蛋炒饭')
else:
    print('我没有钱')

# 循环语句一
money5 = int(input('请输入拥有多少钱'))
print(money5)
while money5 < 300:
    print('我还要努力赚钱')
    money5 += 1
    print(money5)
print('我够钱了，耶！')

# 循环语句二
# （1）
while True:
    content = input('请输入要说的话（’停‘结束循环）：')
    if content == '停':
        break
    print('发送给你：', content)
print('循环结束了')

# （2）
money6 = int(input('请输入拥有多少钱'))
print(money6)
while money6 < 300:
    if money6 == 298:
        money6 += 1
        continue
    print('我还要努力赚钱')
    print(money6)
    money6 += 1

print('我有：', money6, '块钱。我够钱了，耶！')

# for循环
forVal = '这是拿来测试for循环的'
for item in forVal:
    print(item)

# for循环想要计数，必须借助于range
# range(n)，从0数到n，不包含n
# range(m, n)，从m数到n，不包含n
# range(m, n, s)，从m数到n，不包含n,间隔s
for item1 in range(5):
    print('第一个循环：', item1)
print('-------------')
for item2 in range(6, 10):
    print('第二个循环：', item2)
print('-------------')
for item2 in range(0, 10, 2):
    print('第三个循环：', item2)

# pass 代码占位
num = 10
if num > 15:
    pass
print('pass跳过')
