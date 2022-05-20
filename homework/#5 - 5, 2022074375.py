#5 - 5 - (1)
def intersection(xs, ys):
    if xs != []:
        if xs[0] in ys:
            return [xs[0]] + intersection(xs[1:], ys) 
        else:
            return intersection(xs[1:], ys)
    else:
        return xs # or []
    
#5 - 5 - (2)
def intersection(xs, ys):
    def loop(xs, total):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:], total + [xs[0]])
            else:
                return loop(xs[1:], total)
        else:
            return total
    return loop(xs, [])

#5 - 5 - (3)
def intersection(xs, ys):
    total = []
    while xs != []:
        if xs[0] in ys:
            total += [xs[0]]
            xs = xs[1:]
        else:
            xs  = xs[1:]
    return total
    
#5 - 5 - (5)
def intersection(xs, ys):
    total = []
    for _ in range(len(xs)):
        if xs[0] in ys:
            total += [xs[0]]
            xs = xs[1:]
        else:
            xs = xs[1:]
    return total

print(intersection([], []))
print(intersection([1, 2], []))
print(intersection([], [3, 4]))
print(intersection([1, 2], [3, 4]))
print(intersection([1, 2], [2, 3]))
print(intersection([1, 2], [2, 1]))
print(intersection([1, 2, 3], [3, 2, 1]))
print(intersection([1, 2, 3], [3, 2, 4]))
print(intersection([1, 2, 3], [4, 5, 6]))
