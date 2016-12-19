# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:10:39 2016
@author: findys
1002. 写出这个数 (20)
读入一个自然数n，计算其各位数字之和，用汉语拼音写出和的每一位数字。
输入格式：每个测试输入包含1个测试用例，即给出自然数n的值。这里保证n小于10100。
输出格式：在一行内输出n的各位数字之和的每一位，拼音数字间有1 空格，但一行中最后一个拼音数字后没有空格。
输入样例：
1234567890987654321123456789
输出样例：
yi san wu
"""

def main():
    list1 = [0,1,2,3,4,5,6,7,8,9]
    list2 = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
    dict1 = dict(zip(list1,list2))
    list3 = []
    n = input()
    sumN = 0
    while n > 10:
        sumN += n%10
        n /= 10
    sumN += n
    a = 0
    while sumN > 10:
         list3.append(sumN %10)
         sumN /= 10
         a += 1
    list3.append(sumN)
    while len(list3) > 1:
        print dict1[list3.pop()],
    print dict1[list3[0]]
main()
