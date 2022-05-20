def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

def isfixed(s):
    (num, dot, fraction) = s.partition('.')
    return dot == '' and fraction == '' and isinteger(num) or \
           dot == '.' and \
           ((num == '' or num == '-') and fraction.isdigit() or \
           fraction == '' and isinteger(num) or \
           isinteger(num) and fraction.isdigit())

def isfloat(s):
    (significant, e, exponent) = s.partition('e')
    return isfixed(s) or \
           (significant.isdigit() and exponent.isdigit()) or \
           (isfixed(significant) and isfixed(exponent)) or \
           (significant.isdigit() and isfixed(exponent)) or \
           (isfixed(significant) and exponent.isdigit()) 


            
           
           
print(isfloat("2"))       # True
print(isfloat("-2"))      # True
print(isfloat(".112"))    # True
print(isfloat("-.112"))   # True
print(isfloat("3.14"))    # True
print(isfloat("-3.14"))   # True
print(isfloat("5."))      # True
print(isfloat("5.0"))     # True
print(isfloat("-777.0"))  # True
print(isfloat("-777."))   # True
print(isfloat("."))       # False
print(isfloat(".."))      # False
print(isfloat("0e3"))     # True
print(isfloat("1.3e0"))   # True
print(isfloat("0.1e3"))   # True
print(isfloat("1e3"))     # True
print(isfloat("1.314e4")) # True
print(isfloat("-1.1e-2")) # True
print(isfloat(".3e4"))    # True
print(isfloat("2.e-2"))   # True
print(isfloat("0e3"))     # True