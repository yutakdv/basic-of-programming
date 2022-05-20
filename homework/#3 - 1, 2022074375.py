def identical(x, y, z):
    if x == y == z:
        return (x, "triple")
    elif x == y or y == z or x == z:
        return (2 ,"twin")
    else:
        return None

print(identical(2,3,4)) # None
print(identical(2,2,4)) # (2, "twin")
print(identical(2,3,2)) # (2, "twin")
print(identical(2,3,3)) # (3, "twin")
print(identical(3,3,3)) # (3, "triple")


######
def identical(x, y, z):
    if x == y == z:
        return (x, "triple")
    elif x == y:
        return (x, "twin")
    elif y == z:
        return (y, "twin")
    elif x == z:
        return (z, "twin")
    else:
        return None

print(identical(2,3,4)) # None
print(identical(2,2,4)) # (2, "twin")
print(identical(2,3,2)) # (2, "twin")
print(identical(2,3,3)) # (3, "twin")
print(identical(3,3,3)) # (3, "triple")
    