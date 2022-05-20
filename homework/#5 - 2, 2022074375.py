#5 - 2 - (1)
def remove_all(x, xs):
    if xs != []:
        if x == xs[0]:
            return remove_all(x, xs[1:])
        else:
            return [xs[0]] + remove_all(x, xs[1:])
    else:
        return []

#5 - 2 - (2)
def remove_all(x, xs):
    def loop(xs, total):
        if xs != []:
            if x == xs[0]:
                return loop(xs[1:], total)
            else:
                return loop(xs[1:], total + [xs[0]])
        else:
            return total
    return loop(xs, [])

#5 - 2 - (3)
def remove_all(x, xs):
    total = []
    while xs != []:
        if x == xs[0]:
            xs = xs[1:]
        else:
            total += [xs[0]]
            xs = xs[1:]
    return total


print(remove_all(3, []))
print(remove_all(3, [3]))
print(remove_all(3, [3, 3, 3, 3]))
print(remove_all(3, [2]))
print(remove_all(3, [2, 3, 2, 3]))
print(remove_all(3, [2, 2, 2, 3]))
print(remove_all(3, [2, 2, 2, 2]))