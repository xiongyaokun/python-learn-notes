#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 16:34
# @Author  : xiongyaokun
# @Site    : 
# @File    : example002.py
# @Software: PyCharm



"""
Q:企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
求应发放奖金总数？
"""



input = raw_input("请输入销售额（万元）： ")
# commission提成
commission = 0
message = "Your commission is"

# try:
#     income = int(input)
#     if income < 10:
#         commission = income * 0.1
#     elif 10<=income<=20:
#         commission = 10*0.1 + (income-10) * 0.075
#     elif 20<income<=40:
#         commission = 10*0.1 + 10*0.075 + (income-20)*0.05
#     elif 40<income<=60:
#         commission = 10*0.1 + 10*0.075 + 20*0.05 + (income-40)*0.03
#     elif 60<income<=100:
#         commission = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + (income-60)*0.015
#     elif income > 100:
#         commission = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + 40*0.015 + (income-100)*0.01
#     print message, commission
# except:
#     print "Your input is wrong!"


limit = [100,60,40,20,10,0]
rate = [0.1,0.075,0.05,0.03,0.015,0.01]
bonus = 0
income = int(input)
for j in range(len(limit)):
    if income >= limit[j]:
        temp_limit = limit[j:]
        temp_limit.reverse()
        print temp_limit
        for k in range(len(temp_limit)-1):
            bonus += (temp_limit[k+1]-temp_limit[k]) * rate[k]
        print message, bonus + (income-limit[j]) * rate[len(rate)-j-1]
        break