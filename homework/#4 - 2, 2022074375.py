##4 - 2 - (1)

#재귀 함수
def sigma_product_power_of_2(n):
    if n > 0:
        return sigma_product_power_of_2(n - 1) + n * pow(2, n - 1)
    else:
         return 0

#꼬리재귀 함수
def sigma_product_power_of_2(n):
    def loop(n, total):
        if n > 0:
            return loop(n - 1, total + n * pow(2, n - 1))
        else:
            return total
    return loop(n, 0)

#while 루프함수
def sigma_product_power_of_2(n):
    total = 0
    while n > 0:
        total, n = total + n * pow(2, n - 1), n - 1
    return total

print(sigma_product_power_of_2(0))
print(sigma_product_power_of_2(1))
print(sigma_product_power_of_2(2))
print(sigma_product_power_of_2(3))
print(sigma_product_power_of_2(4))
print(sigma_product_power_of_2(5))
print(sigma_product_power_of_2(6))
print(sigma_product_power_of_2(7))

##4 - 1 - (2)
def sigma_product_power_of_2(n):
    return (n - 1) * 2 ** n + 1

# (기초)
# n = 0
# sigma_product_power_of_2(0) = (-1) * 2 ** 0 + 1

# (귀납)
# n >= 0에서
# sigma_product_power_of_2(n) = (n - 1) * 2 ** n + 1임을 보이면 된다.
# sigma_product_power_of_2(n + 1) = (n) * 2 ** (n + 1) + 1
# sigma_product_power_of_2(n + 1) = sigma_product_power_of_2(n) + (n + 1) * pow(2, n)
# sigma_product_power_of_2(n) == (n - 1) * 2 ** n + 1
#  >> (n - 1) * 2 ** n + 1 + (n + 1) * 2 ** n = (n) * 2 ** (n + 1) + 1 (일치하는지 보이면 됨.)
#  >> 2 ** n * (2 * n) + 1 = n * 2 ** (n + 1) + 1
#  >> 2 ** n * (2 * n) + 1 --> n * 2 ** (n + 1) + 1
#  ==> 서로 같다. 