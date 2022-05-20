##실습 3.1
def even(n):
    return n % 2 == 0

print(even(13)) #False
print(even(26)) #True

#------------------------------------------------------------------------------------------------#

##실습 3.2
score = int(input("Enter your score: "))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C') 
elif 60 <= score <= 69:
    print('D')
elif 0 <= score <= 59:
    print('F')
else:
    print('Your score is out of range.')

#------------------------------------------------------------------------------------------------#

##실습 3.3
x = int(input("Enter your number: "))
if x % 2 == 0 and x % 3 == 0:
    print(x, "is divisible by 2 and 3")
elif x % 2 == 0 and not x % 3 == 0:
    print(x, "is divisible by 2 but not by 3")
elif not x % 2 == 0 and x % 3 == 0:
    print(x, "is divisible by 3 but not by 2")
else:
    print(x, "is not divisible by 2 or 3")

#------------------------------------------------------------------------------------------------#

##실습 3.4
def smaller(x, y):
    if x < y:
        return x
    else:
        return y 

print(smaller(3, 5)) # 3
print(smaller(5, 3)) # 3
print(smaller(3, 3)) # 3

#------------------------------------------------------------------------------------------------#

##실습 3.5
def smallest(x, y, z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

print(smallest('__, __, __')) #아무 숫자나 들어가도 셋 중 가장 작은 값이 출력된다.

#------------------------------------------------------------------------------------------------#

##실습 3.6

def smaller(x, y):
    if x < y:
        return x
    else:
        return y

def smallest(x, y, z):
    return smaller(smaller(x, y), z)

#------------------------------------------------------------------------------------------------#

#3.3.1 무조건 반복

#code
from math import pi

def area_circle(radius, n):
    if radius > 0:
        area = pi * radius ** 2
        return round(area, n)
    else:
        return 0.0

print("Circle Area Calculator")
r = int(input("Radius? "))
p = int(input("Precision? "))
area = area_circle(r, p)
print("The area of a circle with radius %d is %d." %(r,area))

#same code // #just 무한 루프 // 프로그램이 종료되지 않고 게속 실행된다.
from math import pi

def area_circle(radius, n):
    if radius > 0:
        area = pi * radius ** 2
        return round(area, n)
    else:
        return 0.0

print("Circle Area Calculator")
#while True:
#    r = int(input("Radius? "))
#    p = int(input("Precision? "))
#    area = area_circle(r, p)
#    print("The area of a circle with radius %d is %d." %(r, area))

#------------------------------------------------------------------------------------------------#

##실습 3.7
print("Score Average Calculator")
total = 0 
count = 0
number = int(input("How many classes: "))
while count < number:
    score = int(input("Enter your score: "))
    total = total + score
    count += 1

if count > 0:
    print("Your average score = ", round(total / number, 1))
else:
    print("Your average score = 0.0")

#------------------------------------------------------------------------------------------------#

##3-14.py
from math import pi

def area_circle(radius, n):
    if radius > 0:
        area = pi * radius ** 2
        return round(area, n)
    else:
        return 0.0

print("Circle Area Calculator")
more = 'y'
while more == 'y':
    r = input("Radius? ")
    while not r.isdigit():
        r = input("Radius? ")
    p = input("Precision? ")
    while not p.isdigit():
        p = input("Precision? ")
    area = area_circle(int(r), int(p))
    print("The area of a circle with radius", r, "is", area, ".")
    more = input("Press y to continue, any other key to exit.")
print("Please come back again.")

#------------------------------------------------------------------------------------------------#

##실습 3.8
print("Score Average Calculator")
number = input("How many classes? ")
while not (number.isdigit() and int(number) > 0):
    number = input("Enter a positive number: ")
print("The number of classes = ", number)

count = 0
total = 0
while count < int(number):
    score = input("Enter your score: ")
    while not (score.isdigit() and 0 <= int(score) <= 100):
        score = input("Enter your score between 0 and 100: ")
    print("Your score = ", score)
    total = total + int(score)
    count += 1

if count > 0:
    print("Your average score = ", round(total / int(number), 1))
else:
    print("Youre average score = 0.0")

#------------------------------------------------------------------------------------------------#

##실습 3.9
def is_integer(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

#------------------------------------------------------------------------------------------------#

##실습 3.10
def is_integer(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

def is_float(s):
    (num, dot, fraction) = s.partition('.')
    return dot == '' and fraction == '' and is_integer(num) or \
            dot == '.' and \
            ((num == '' or num == '-') and fraction.isdigit() or \
            fraction == '' and is_integer(num) or \
            is_integer(num) and fraction.isdigit())

#----------------------------------연습문제--------------------------------------------------#

##3.1
def isleapyear(year):
    if year >= 0:
        return year % 400 == 0 or \
               year % 4 == 0 and year % 100 != 0
    else:
        return None

#same code
def isleapyear(year):
     if year >= 0:
         if year % 4 == 0:
             if year % 100 == 0 and not year % 400 == 0:
                 return False
             else:
                 return True
         else:
             return False
     else:
         return None

#test code
for x in range(5):
    print(x, isleapyear(x))

for x in range(2010, 2017):
    print(x, isleapyear(x))

for x in range(1900, 2500, 100):
    print(x, isleapyear(x))

print(isleapyear(2020))
print(isleapyear(-2000))

#----------------------------------연습문제--------------------------------------------------#

##3.2  #my code
def is_valid_date(year, month, day):
    if year >= 0 and 1 <= month <= 12:
        if year % 400 == 0 or \
                year % 4 == 0 and year % 100 != 0:
            if month == 2:
                return day <= 29
        if month % 2 == 0:
            if 1 <= month <= 7:
                if month == 2:
                    return day <= 28
                else:
                    return day <= 30
            else:
                return day <= 31
        else:
            if 1<= month <= 7:
                return day <= 31
            else:
                return day <= 30
    
    
#answer code => same code
def is_valid_date(year,month,day):
    return year >= 0 and 1 <= month <= 12 and \
           ((month == 1 or month == 3 or month == 5 or month == 7 or
             month == 8 or month == 10 or month == 12) and 
            1 <= day <= 31 or 
            (month == 4 or month == 6 or month == 9 or month == 11) and 
            1 <= day <= 30 or 
            isleapyear(year) and 1 <= day <= 29 or 
            1 <= day <= 28) 

#----------------------------------연습문제--------------------------------------------------#

##3.3  #주민등록번호 검증 함수#
def isleapyear(year):
    if year >= 0:
        return year % 400 == 0 or \
               year % 4 == 0 and year % 100 != 0
    else:
        return None

def is_valid_date(year,month,day):
    return year >= 0 and 1 <= month <= 12 and \
           ((month == 1 or month == 3 or month == 5 or month == 7 or
             month == 8 or month == 10 or month == 12) and 
            1 <= day <= 31 or 
            (month == 4 or month == 6 or month == 9 or month == 11) and 
            1 <= day <= 30 or 
            isleapyear(year) and 1 <= day <= 29 or 
            1 <= day <= 28) 
            
def front_OK(s):
    year = int(s[:2])
    month = int(s[2:4])
    day = int(s[4:6])
    century = s[-1]
    if century == 1 or century == 2 or century == 5 or century == 6:
        year = year + 1900
    elif century == 3 or century == 4 or century == 7 or century == 8:
        year = year + 2000
    elif century == 9 or century == 0:
        year = year + 1800
    return is_valid_date(year, month, day)

def back_OK(s):
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    e = int(s[4])
    f = int(s[5])
    g = int(s[7])
    h = int(s[8])
    i = int(s[9])
    j = int(s[10])
    k = int(s[11])
    l = int(s[12])
    m = 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11)
    if m == 10 or m == 11:
        m = m - 10
    return m == int(s[13])

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_OK(front + back[0]) and mid == "-" and back_OK(s)

#----------------------------------연습문제--------------------------------------------------#

##3.4
def smaller(x, y):
    if x < y:
        return x
    else:
        return y

def smallest(x, y, z):
    return smaller(smaller(x, y), z)

def median(x, y, z):
    one = smallest(x, y, z)
    if one == x:
        return smaller(y, z)
    elif one == y:
        return smaller(x, z)
    else:
        return smaller(x, y)

#----------------------------------연습문제--------------------------------------------------#

##3.5
def even(x):
    return x % 2 == 0

def smaller_odd(x, y):
    if x < y and x % 2 == 1:
        return x
    elif x > y and y % 2 == 1:
        return y
    else:
        return None

#same code (smaller_odd) // using def even(x)
def smaller_odd(x, y):
    if even(x) and even(y):
        return None
    elif even(x):
        return x
    elif even(y):
        return y
    else:
        if x < y:
            return x
        else:
            return y

def smallest_odd(x, y, z):
    smaller = smaller_odd(x, y)
    if smaller == None:
        if even(z):
            return None
        else:
            return z
    else:
        return smaller_odd(smaller, z)

#----------------------------------연습문제--------------------------------------------------#

##3.6   #my code
from math import sqrt

def quadratic_equation_positive(a, b, c):
    if a != 0:
        if b ** 2 - 4 * a * c < 0:
            return None
        else:
            print((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    else:
        return None

#answer code
from math import sqrt

def quadratic_equation_positive(a, b, c):
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            root = sqrt(delta)
            return (-b + root) / (2 * a), (-b - root) / (2 * a)
        else:
            return None

#----------------------------------연습문제--------------------------------------------------#

##3.7   #my code
print("Score Average Calculator")
classes = int(input("How many classes? "))
if classes > 0:
    print("The number of classes =", classes)
count = 0
total = 0
Failed = 0
while count < classes:
    score = int(input("Enter your score: "))
    print("Your score =", score)
    if 1 <= score <= 59:
        Failed += 1
    else:
        total = total + score
    count += 1

print("Your average score =", round(total / (count - Failed), 1))
print("Failed = ", Failed)

#answer code
print("Score Average Calculator")
number = input("How many classes? ")
while not (number.isdigit() and int(number) > 0):
    number = input("Enter a positive number: ")
print("The number of classes =", number)
total = 0
passed = 0
failed = 0
while passed + failed < int(number):
    score = input("Enter your score: ")
    while not (score.isdigit() and 0 <= int(score) <= 100):
        score = input("Enter your score between 0 and 100: ")
    print("Your score =", score)
    if int(score) < 60:
        failed = failed + 1
    else:
        total = total + int(score)
        passed = passed + 1
if passed > 0:
    print("Your average score =", round(total/passed,1))
else:
    print("Your average score = 0.0")
print("Failed =", failed)

#----------------------------------연습문제--------------------------------------------------#

##3.8 
def validclock24(time):
    (hour, colon, minute) = time.partition(":")
    return len(hour) == 2 and len(minute) == 2 and colon == ":" and 0 <= int(hour) <= 23 and \
           0 <= int(minute) <= 59 or int(hour) == 24 and int(minute) == 0 

print(validclock24("00:00"))
print(validclock24("00:30"))  
print(validclock24("09:58"))  
print(validclock24("12:15"))  
print(validclock24("23:59"))  
print(validclock24("24:00"))  
print(validclock24("7:07"))   
print(validclock24("07:121")) 
print(validclock24("13:4"))   
print(validclock24("00:60"))  
print(validclock24("24:01"))  
print(validclock24("25:10"))

#----------------------------------연습문제--------------------------------------------------#

##3.9
def validclock12(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]
    return (len(hour) == 1 and 1 <= int(hour) <= 9 or \
           len(hour) == 2 and 10 <= int(hour) <= 12) and \
           colon == ":" and \
           len(minute) == 2 and 0 <= int(minute) <= 59 and \
           (am_or_pm == "am" or am_or_pm == "pm") 

print(validclock12("1:30am"))  
print(validclock12("9:12pm"))  
print(validclock12("3:05am"))  
print(validclock12("10:14pm"))  
print(validclock12("11:59pm"))  
print(validclock12("12:00am")) 
print(validclock12("12:00pm")) 
print(validclock12("0:15am"))  
print(validclock12("09:18pm")) 
print(validclock12("3:5am"))   
print(validclock12("00:00pm")) 
print(validclock12("5:60am"))  

#----------------------------------연습문제--------------------------------------------------#

##3.10 ##my code
def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    if len(hour) == 2 and 0 <= int(hour) and 0 <= int(minute) <= 59 and len(minute) == 2:
        if 13 <= int(hour) <= 23:
            return str(int(hour) - 12) + colon + minute + "pm"
        elif 1 <= int(hour) <= 11:
            return str(int(hour)) + colon + minute + "am"
        elif int(hour) == 12:
            if int(minute) >= 0:
                return str(int(hour)) + colon + minute + "pm"
        elif int(hour) == 24:
            return str(int(hour) - 12) + colon + minute + "am"
        elif int(hour) == 0:
            return str(int(hour) + 12) + colon + minute + "am"
    else:
        return 'Fail'
    return time
            
#answer code -----> this code cannot catch minus hour ㅜ.ㅜ
def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    if len(hour) == 2:
        if int(hour) == 0 or int(hour) == 24:
            return "12" + colon + minute + "am"
        elif int(hour) < 12:
            return hour + colon + minute + "am"
        elif int(hour) == 12:
            return hour + colon + minute + "pm" 
        else: # int(hour) > 12
            return str(int(hour)-12) + colon + minute + "pm"

#----------------------------------연습문제--------------------------------------------------#

##3.11
def clock24to12(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]
    if am_or_pm == 'am' and hour == "12":
        hour = "00" 
    elif am_or_pm == 'pm':
        if hour == "12":
            hour = "12"
        else:
            hour = str(int(hour) + 12)
    if len(hour) < 2:
        hour = "0" + hour
    return hour + colon + minute

#----------------------------------연습문제--------------------------------------------------#

##3.12
    
def minutes_after(time, minuteplus):
    (hour, colon, minute) = time.partition(":")
    hourplus = minuteplus // 60
    minuteplus = minuteplus % 60
    hour = int(hour) + hourplus
    minute = int(minute) + minuteplus
    if minute > 59:
        hour = hour + 1
        minute = minute - 60
        
    return str(hour) + colon + str(minute)

#----------------------------------연습문제--------------------------------------------------#

##3.13
def time_passed(fromtime, totime):
    (hour1, colon, minute1) = fromtime.partition(":")
    (hour2, colon, minute2) = totime.partition(":")
    hour = int(hour2) - int(hour1)
    if minute1 > minute2:
        hour = hour - 1
        minute = int(minute2) + 60 - int(minute1)
    else:
        minute = int(minute2) - int(minute1)
    return str(hour) + colon + str(minute)

#----------------------------------연습문제--------------------------------------------------#

##3.14

def addtime(time1, time2):
    (hour1, colon, time1) = time1.partition(":")
    (minute1, colon, second1) = time1.partition(":")
    (hour2, colon, time2)  = time2.partition(":")
    (minute2, colon, second2) = time2.partiton(":")
    hour = int(hour2) + int(hour1)
    minute = int(minute1) + int(minute2)
    second = int(second1) + int(second2)
    if second >= 60:
        second = second - 60
        minute = minute + 1
    if minute >= 60:
        minute = minute - 60
        hour = hour + 1
    if minute < 10:
        minute =  "0" + str(minute)
    if second < 10:
        second =  "0" + str(second)
    else:
        second = str(second)
    return str(hour) + colon + str(minute) + colon + str(second)



print(addtime("0:13:57", "0:25:02")) # "0:39:59"

#----------------------------------연습문제--------------------------------------------------#

##3.15


                
        
