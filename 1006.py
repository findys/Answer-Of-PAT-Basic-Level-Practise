# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:35:35 2016

@author: findys
1006. 换个格式输出整数 (15)
让我们用字母B来表示“百”、字母S表示“十”，用“12...n”来表示个位数字n（<10），换个格式来输出任一个不超过3位的正整数。
例如234应该被输出为BBSSS1234，因为它有2个“百”、3个“十”、以及个位的4。
输入格式：每个测试输入包含1个测试用例，给出正整数n（<1000）。
输出格式：每个测试用例的输出占一行，用规定的格式输出n。
输入样例1：
234
输出样例1：
BBSSS1234
"""

def main():
    list1 = []
    list2 = []
    n = input()
    list1.append(n/100)
    list1.append(n%100/10)
    list1.append(n%10)
    for i in range(list1[0]):
        list2.append('B')
    for i in range(list1[1]):
        list2.append('S')
    for i in range(list1[2]):
        list2.append(str(i+1))
    print ''.join(list2)
main()