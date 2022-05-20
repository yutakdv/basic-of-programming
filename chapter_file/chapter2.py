##실습 2.1
from math import pi
radius = int(input())
area = pi * radius ** 2
print("The area of a circle with radius", radius, "is", round(area, 1))

#------------------------------------------------------------------------------------------------#

##실습 2.2
print("Enter the number of coins you have.")
c500 = int(input("500 won? "))
c100 = int(input("100 won? "))
c50 = int(input("50 won? "))
c10 = int(input("10 won? "))
total = c500 * 500 + c100 * 100 + c50 * 50 + c10 * 10

print("You have %d won in total." %total)

#------------------------------------------------------------------------------------------------#

##실습 2.3
print("Fahrenheit to Celsius conversion")
f = int(input("Degrees in Fahrenheit?"))
print(round((f - 32) * 5 / 9, 1), "degrees in Celsius")

#------------------------------------------------------------------------------------------------#

##실습 2.4
def coin_in_total(c500, c100, c50, c10):
    total = c500 * 500 + c100 * 100 + c50 * 50 + c10 * 10
    return total

print(coin_in_total(4, 2, 3, 4))
#------------------------------------------------------------------------------------------------#

##실습 2.5
def fahrenheit2celsius(f):
    return (f - 32) * 5 / 9

print(fahrenheit2celsius(67))
print(round(fahrenheit2celsius(69), 1)) 

#------------------------------------------------------------------------------------------------#

##실습 2.6
def complement_nine(n):
    return 10 ** len(str(n)) - 1 - n

print(complement_nine(0)) 
print(complement_nine(9))
print(complement_nine(4))
print(complement_nine(18))
print(complement_nine(40))
print(complement_nine(307))
print(complement_nine(9142))
print(complement_nine(9965))
print(complement_nine(9999))

#------------------------------------------------------------------------------------------------#

##2.1
def celsius2fahrenheit(c):
    return 9 / 5 * c + 32

print(celsius2fahrenheit(19.4))
print(round(celsius2fahrenheit(19.4), 1))

#------------------------------------------------------------------------------------------------#

##2.2 (가)
def monthly_payment_plan(principal, interest, year):
     rate_monthly = interest / 100 /12
     compound = (1 + rate_monthly) ** (year * 12)
     return int(compound * principal * rate_monthly / (compound - 1))

print(monthly_payment_plan(10000000, 2.8, 4))

#------------------------------------------------------------------------------------------------#

##2.2 (나)
print("자유은행 대출 상환금 계산 서비스에 오심을 환영합니다.")
principal = int(input("대출원금이 얼마인가요?(백만원 이상)"))
interest = float((input("연 이자율은 몇 %인가요?(0.0 ~ 9.9)")))
year = int(input("상환기간은 몇 년인가요?"))

#상환금 계산
rate_yearly = interest / 100
rate_monthly = rate_yearly / 12
month = year * 12
compound = (1 + rate_monthly) ** month
payment_monthly = int(compound * principal * rate_monthly / (compound - 1))

print()
print("대출 상환금 내역을 알려드리겠습니다.")
print("대출원금:", principal, "원")
print("연 이자율", interest, "매월", payment_monthly, "원씩 지불하셔야 합니다.")
print("상환 완료시까지 총 상환금액은", payment_monthly * 12 * year, "원입니다.")
print()
print("저희 자유은행은 항상 여러분과 함꼐 합니다.")
print("또 들려주세요.")