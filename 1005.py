# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:42:56 2016
@author: findys
1005. 继续(3n+1)猜想 (25)
卡拉兹(Callatz)猜想已经在1001中给出了描述。在这个题目里，情况稍微有些复杂。
当我们验证卡拉兹猜想的时候，为了避免重复计算，可以记录下递推过程中遇到的每一个数。例如对n=3进行验证的时候，我们需要计算3、5、8、4、2、1，则当我们对n=5、8、4、2进行验证的时候，
就可以直接判定卡拉兹猜想的真伪，而不需要重复计算，因为这4个数已经在验证3的时候遇到过了，我们称5、8、4、2是被3“覆盖”的数。我们称一个数列中的某个数n为“关键数”，如果n不能被数列
中的其他数字所覆盖。
现在给定一系列待验证的数字，我们只需要验证其中的几个关键数，就可以不必再重复验证余下的数字。你的任务就是找出这些关键数字，并按从大到小的顺序输出它们。
输入格式：每个测试输入包含1个测试用例，第1行给出一个正整数K(<100)，第2行给出K个互不相同的待验证的正整数n(1<n<=100)的值，数字间用空格隔开。
"""

def main():
    n = input()
    list1 = []
    list2 = []
    list3 = []
    list1 = map(int, raw_input().split())
    for i in range(0, len(list1)):
        listw = []
        n = list1[i]
        if n == 1:
            listw.append(1)
        else:
            listw.append(n)
            while n > 1:
                if n % 2 == 0:
                    n = n / 2
                    listw.append(n)
                else:
                    n = (n * 3 + 1) / 2
                    listw.append(n)
        list2.append(listw)
    for i in range(len(list1)):
        count = 0
        for j in range(len(list1)):
            if i == j:
                continue
            else:
                if set(list2[i]).issubset(set(list2[j])):
                    break
                else:
                    count += 1
        if count == len(list1) - 1:
            list3.append(list1[i])
    list3.sort()
    while len(list3) > 1:
        print list3.pop(),
    print list3.pop()

main()
