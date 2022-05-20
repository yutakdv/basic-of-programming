from re import I


def seq_search_OX(s, x):
    if s != []:
        if s[0] == x:
            return True
        else:
            return seq_search_OX(s[1:], x)
    else:
        return False

#while 루프 버전
def seq_search_OX(s, x):
    while s!= []:
        if s[0] == x:
            return True
        else:
            s = s[1:]
    return False

#for 루프 버전
def seq_search_OX(s, x):
    for key in s:
        if key == x:
            return True
    return False

#논리연산자 버전
def seq_search_OX(s, x):
    return s != [] and s[0] == x or seq_search_OX(s[1:], x)

#재귀 함수
def seq_search_OX(s, x):
    def loop(s, i):
        if s != []:
            if s[0] == x:
                return i 
            else:
                return loop(s[1:], i + 1)
        else:
            return None
    return loop(s, 0)

def seq_search(s, x):
    def loop(i):
        if i < len(s):
            if s[i] == x:
                return i 
            else:
                return loop(i + 1)
        else:
            return None
    return loop(0)

#test code
print(seq_search([3, 5, 4, 2], 4))

#while 루프 버전
def seq_search(s, x):
    i = 0
    while i < len(s):
        if s[i] == x:
            return i
        else:
            i += 1
    return None

#for 루프 버전
def seq_search(s, x):
    for i in range(len(s)):
        if s[i] == x:
            return i
    return None

##이분탐색
def bin_search_OX(ss, x):
    if ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            return bin_search_OX(ss[:mid], x)
        else:
            return bin_search_OX(ss[mid + 1], x)
    else:
        return False


#while 루프 버전
def bin_search_OX(ss, x):
    while ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            ss = ss[:mid]
        else:
            ss = ss[mid + 1:]
    return False

#논리연산자 버전
def bin_search_OX(ss, x):
    mid = len(ss) // 3
    return ss != [] and \
           (x == ss[mid] or 
            x < ss[mid] and bin_search_OX(ss[:mid], x) or
            x > ss[mid] and bin_search_OX(ss[mid + 1:], x))

# Test code
s = [3,5,8,7,4,6,1,9,2]
s.sort()
print(bin_search_OX(s,5))
print(bin_search_OX(s,8))
print(bin_search_OX(s,1))
print(bin_search_OX(s,11))

#이분 탐색
#범위 둘로 나누어서 계산 
#low, high, mid -> mid 기준으로 up, down 

def bin_search(ss, x):
    low = 0
    high = len(ss) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == ss[mid]:
            return mid
        elif x < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

## import 모듈 -> random
import random
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

## 검색 키 뽑기
import random
print(random.randrange(20))
print(random.randrange(20))
print(random.randrange(20))

## 함수 호출의 실행 시간 측정
import time
print("Now, go!")
start = time.perf_counter()
print("Start at", start)
time.sleep(5)
finish = time.perf_counter()
print("Finish at", finish)
print("Total =", finish - start, "seconds")

## 실행 시간 비교 테스트 코드 작성
from random import sample, randrange
from time import perf_counter

print("Preparing data for seq_search. Please, wait a moment ...")
data = sample(range(10000000), 8000000)

print("Testing seq_search function begins ...")
for _ in range(10):
    x = randrange(10000000)
    start = perf_counter()
    index = seq_search(data, x)
    finish = perf_counter()
    print(x, "is found at", index, "in", finish - start, "seconds")

print("Preparing data for bin_search. Please, wait a moment ...")
data.sort()

print("Testing bin_search function begins ...")
for _ in range(10):
    x = randrange(10000000)
    start = perf_counter()
    index = bin_search(data, x)
    finish = perf_counter()
    print(x, "is found at", index, "in", finish - start, "seconds")

text = "Your time is limited, so don't waste it living someone else's life"
print(text.find("me")) # 7
print(text.find("li")) # 13
print(text.find("live")) # -1
print(text.rfind("me")) # 49
print(text.rfind("li")) # 62

text = "Individual Freedom"
print(text.startswith("I"))
print(text.startswith("Indian"))
print(text.endswith("dom"))
print(text.endswith("Free"))

text = "Your time is limited, so don't waste it living someone else's life."
print(text.find("me"))
print(text.find("me", 8))
print(text.find("me", 8, 49))

## 처음 나타나는 문자열 하나만 찾기
def find_1st(filename, x):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(x)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 1st time.\n")
    outfile.close()
    infile.close()
    print("Done")

print(find_1st('article.txt', 'computer')) # computer is at 3269 the 1st time.
print(find_1st('article.txt', 'Whole Earth')) # Whole Earth is at 10735 the 1st time.
print(find_1st('article.txt', 'Apple')) # Apple is at 4380 the 1st time.
print(find_1st('article.txt', 'apple')) # apple is not found.

def find_2nd(filename, x):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    position = text.find(x, position + 1)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 2nd time.\n")
    outfile.close()
    infile.close()
    print("Done")

print(find_2nd('article.txt', 'computer')) # computer is at 3357 the 2nd time.
print(find_2nd('article.txt', 'Whole Earth')) # Whole Earth is at 11280 the 2nd time.
print(find_2nd('article.txt', 'Apple')) # Apple is at 4455 the 2nd time.
print(find_2nd('article.txt', 'apple')) # apple is not found.

# 마지막 문자열 하나만 찾기.
def find_last(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    lastPosition = -1
    position = text.find(key)
    while position != -1 :
        lastPosition = position
        position = text.find(key,position+1)
    if lastPosition == -1:
        outfile.write(key + " is not found.\n")
    else:
        outfile.write(key + " is at " + str(lastPosition) + " the last time.\n")
    outfile.close()
    infile.close()
    print("Done")

# Test code
print(find_last('article.txt','computer'))    # at 10975 the last time.
print(find_last('article.txt','Whole Earth')) # at 11280 the last time.
print(find_last('article.txt','Apple'))       # at 6604 the last time.
print(find_last('article.txt','apple'))       # not found.

# 모두 찾기
def find_all(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key + " is not found.\n")
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        position = text.find(key,position+1)
    outfile.close()
    infile.close()
    print("Done")

# Test code
print(find_all('article.txt','computer')) # computer is at 3269, 3357, 3601, 3725, 6209, 10975.
print(find_all('article.txt','Whole Earth')) # Whole Earth is at 10735, 11280.
print(find_all('article.txt','Apple')) # Apple is at 4380, 4455, 4742, 5586, 5765, 6346, 6379, 6445, 6604.
print(find_all('article.txt','apple')) # apple is not found

# 모두 찾고, 개수 세기
def find_all_count(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        count += 1
        position = text.find(key,position+1)
    outfile.write(key + " is found " + str(count) + " time(s).\n")
    outfile.close()
    infile.close()
    print("Done")

# Test code
print(find_all_count('article.txt','computer'))     # 6 time(s).
print(find_all_count('article.txt','Whole Earth'))  # 2 time(s).
print(find_all_count('article.txt','Apple'))        # 9 time(s).
print(find_all_count('article.txt','commencement')) # 1 time(s).
print(find_all_count('article.txt','apple'))       # 0 time(s).


