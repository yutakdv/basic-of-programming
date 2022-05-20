#5 - 6 - (1)
def difference(xs, ys):
    if xs != []:
        if xs[0] in ys:
            return difference(xs[1:], ys)
        else:
            return [xs[0]] + difference(xs[1:], ys)
    else:
        return xs #or []

#5 - 6 - (2)
def difference(xs, ys):
    def loop(xs, total):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:], total)
            else:
                return loop(xs[1:], total + [xs[0]])
        else:
            return total
    return loop(xs, [])

#5 - 6 - (3)
def difference(xs, ys):
    total = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            total += [xs[0]]
            xs = xs[1:]
    return total

#5 - 6 - (4)
def difference(xs, ys):
    total = []
    for _ in range(len(xs)):
        if xs[0] in ys:
            xs = xs[1:]
        else:
            total += [xs[0]]
            xs = xs[1:]
    return total

print(difference([], []))
print(difference([1, 2], []))
print(difference([], [3, 4]))
print(difference([1, 2], [3, 4]))
print(difference([1, 2], [2, 3]))
print(difference([1, 2], [2, 1]))
print(difference([1, 2, 3], [3, 2, 1]))
print(difference([1, 2, 3], [3, 2, 4]))
print(difference([1, 2, 3], [4, 5, 6]))
