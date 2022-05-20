#5 - 1 - (1)
def remove_one(x, xs):
    if xs != []:
        if x == xs[0]:
            return xs[1:]
        else:
            return [xs[0]] + remove_one(x, xs[1:])
    else:
        return []

#5 - 1 - (2)
def remove_one(x, xs):
    def loop(xs, total):
        if xs != []:
            if x == xs[0]:
                return total + xs[1:]
            else:
                return loop(xs[1:], total + [xs[0]])
        else:
            return total
    return loop(xs, [])

#5 - 1 - (3)
def remove_one(x, xs):
    total = []
    while xs != []:
        if x == xs[0]:
            xs = xs[1:]
            total += xs
            break
        else:
            total += [xs[0]]
            xs = xs[1:]
    return total

print(remove_one(3, []))
print(remove_one(3, [3]))
print(remove_one(3, [2]))
print(remove_one(3, [2, 3, 2, 3]))
print(remove_one(3, [2, 2, 2, 3]))
print(remove_one(3, [2, 2, 2, 2]))
