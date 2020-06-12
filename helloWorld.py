#!/usr/bin/python3
import sys

print("Hello World!")

if True:
    print("True")

# 这是一行注释
'''
else:
    print('False')
'''

# string = input("\n\n输入回车后退出")

x = 'runoob'
sys.stdout.write(x + '\n')

y = 123.0
isinstance(y, int)

print(y)
print(x)
print(y)

# 字符串截取
string = 'abcdefg'

print('string[0]' + string[0])
print('string[0:-1]' + string[0:-1])
print('string[0:5]' + string[0:5])
print('string[2:-1]' + string[2:-1])
print('string[2:5]' + string[2:5])
print('string[2:-3]' + string[2:-3])
print('string * 2' + string * 2)

# list列表获取
listData = [1, 'b', 'c', 'd', 'e', 'f', 'h']
print(listData[0:1])
print(listData[0:2])
print(listData[0:-1])
print(listData[2:-4])
print(listData[2:-2])
print(listData[2:])
print(listData[:])


def reverseWord(inputStr):
    # 通过空格将字符串分隔符, 把各个单词划分为列表
    inputWords = inputStr.split(" ")

    # 翻转字符串
    # 假设列表设置为list = [1, 2, 3, 4]
    # list[0] = 1, list[1] = 2, 而list[-1]表示最后一个元素 list[-1] = 4, 等价于list[3] = 4
    # inputWord[-1::-1], 则表示从倒数第一格元素获取, 获取到字段头, 第三个参数-1指的是反向
    inputWords = inputWords[-1::-3]

    # 重新组合字符串
    output = ' '.join(inputWords)
    return output
    pass


if __name__ == "__main__":
    inputWord = 'hi, you know, I prefer like you.'
    rw = reverseWord(inputWord)
    print(rw)
