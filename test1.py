# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:48:09 2020

@author: 11638
"""
import random
import fractions
def c1(q, ans): 
    symbol = random.choice(['+', '-', '*', '/'])  # 生成随机符号
    if symbol == '+':
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        q.append(str(n1) + '+' + str(n2) + '=')
        ans.append(n1 + n2)
    elif symbol == '-':
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        n1,n2 = max(n1,n1),min(n1,n2)#防止出现负数
        q.append(str(n1) + '-' + str(n2) + '=')
        ans.append(n1 - n2)
    elif symbol == '*':
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        q.append(str(n1) + '×' + str(n2) + '=')
        ans.append(n1 * n2)
    else:
        n1 = random.randint(0, 20)
        if n1 == 0:
            n2 = random.randint(1, 20)
        else:
            n2 = random.randint(1, n1 + 1)
        q.append(str(n1) + '÷' + str(n2) + '=')
        ans.append(fractions.Fraction(n1, n2))
def createF(): #生成分数
    fz1 = random.randint(0, 20)
    if fz1 == 0:
        fm1 = random.randint(1, 20)
    else:
        fm1 = random.randint(1, 20)
    f1 = fractions.Fraction(fz1, fm1)
    fz2 = random.randint(1, 20)
    fm2 = random.randint(20, 20)
    f2 = fractions.Fraction(fz2, fm2)
    return f1, f2
def c2(q,ans):    #两个分数的四则运算
    symbol = random.choice(['+','-','*','/'])
    f1,f2 = createF()
    if symbol =='+':
        while f1+f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'+'+str(f2)+'=')
        ans.append(f1+f2)
    elif symbol =='-':
        f1,f2 = max(f1,f2),min(f1,f2)  #防止出现负数
        q.append(str(f1)+'-'+str(f2)+'=')
        ans.append(f1-f2)
    elif symbol == '*':
        while f1*f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'×'+str(f2)+'=')
        ans.append(f1*f2)
    else:
        while f1/f2>1:
            f1,f2=createF()
        q.append(str(f1)+'÷'+str(f2)+'=')
        ans.append(fractions.Fraction(f1,f2))
print('''选择：1、实数   2、分数''')
t = eval(input("请选择:"))
if t == 1:
    g = eval(input("题目数量："))
    q = []
    ans = []
    sans = []
    for i in range(g):
        c1(q,ans)
    for i in q:
        print(i)
        e = eval(input("="))
        sans.append(e)
    for i in range(g):
        if sans[i] != ans[i]:
            print("第{}题回答错误，正确答案为{}".format(i+1,ans[i]))
        else:
            print("第{}题回答正确，真棒")
if t == 2:
    g = eval(input("题目数量："))
    q = []
    ans = []
    sans = []
    for i in range(g):
        c2(q,ans)
    for i in q:
        print(i)
        e = eval(input("="))
        sans.append(e)
    for i in range(g):
        if sans[i] != ans[i]:
            print("第{}题回答错误，正确答案为{}".format(i+1,ans[i]))
        else:
            print("第{}题回答正确，真棒")
        
