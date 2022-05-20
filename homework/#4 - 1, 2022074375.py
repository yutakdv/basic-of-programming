##4 -1 - (1)

#재귀 함수
def sigma_power_of_2(n):
    if n > 0:
        return sigma_power_of_2(n - 1) + 2 ** n
    else:
        return 2 ** n

#꼬리재귀 함수
def sigma_power_of_2(n):
    def loop(n, total):
        if n > 0:
            return loop(n - 1, 2 ** n + total)
        else:
            return 2 ** n + total
    return loop(n, 0)

#while 루프 함수
def sigma_power_of_2(n):
    total = 0
    while n > 0:
        total, n = total + 2 ** n, n - 1
    return total + 2 ** n


# Test code
print(sigma_power_of_2(0)) # 1
print(sigma_power_of_2(1)) # 3
print(sigma_power_of_2(2)) # 7
print(sigma_power_of_2(3)) # 15
print(sigma_power_of_2(4)) # 31
print(sigma_power_of_2(5)) # 63
print(sigma_power_of_2(6)) # 127
print(sigma_power_of_2(7)) # 255

##4 - 1 - (2)
def sigma_power_of_2(n):
    return 2 ** (n + 1) - 1

# (기초)
# n = 0
# sigma_power_of_2(0) == 2 ** 1 - 1

# (귀납)
# n >= 0에서
# sigma_power_of_2(n) = 2 ** (n + 1) - 1임을 보이면 된다.
# sigma_power_of_2(n + 1) = 2 ** (n + 2) - 1
# sigma_power_of_2(n + 1) = sigma_power_of_2(n) + 2 ** (n + 1)
# >> 2 ** (n + 1) - 1 + 2 ** (n + 1) == 2 ** (n + 2) - 1  (일치하는지 보이면 됨.)
# >> 2 * 2 ** (n + 1) - 1 == 2 ** (n + 2) - 1
# >> 2 * 2 ** (n + 1) -> 2 ** (n + 2)
# ==> 서로 같다.