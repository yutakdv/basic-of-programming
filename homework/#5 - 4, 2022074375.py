#5 - 4 - (1) 
def union(xs,ys) :
    if xs != []:
        if xs[0] in ys:
            return union(xs[1:],ys)
        else:
            head = xs[0]
            return [head] + union(xs[1:],ys)
    else:
        return ys
    
#5 - 4 - (2)
def union(xs, ys):
    def loop(xs, total):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:], total)
            else:
                head = xs[0]
                return loop(xs[1:], total + [head])
        else:
            return total + ys
    return loop(xs, [])

#5 - 4 - (3)
def union(xs, ys):
    total = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            head = xs[0] 
            xs, total = xs[1:], total + [head]
    return total + ys

#5 - 4 - (4)
def union(xs, ys):
    total = []
    for _ in range(len(xs)):
        if xs[0] in ys:
            xs = xs[1:]
        else:
            head = xs[0]
            xs, total = xs[1:], total + [head]
    return total + ys
    
print(union([],[]))
print(union([1, 2], []))
print(union([], [3, 4]))
print(union([1, 2], [3, 4]))
print(union([1, 2], [2, 3]))
print(union([1, 2], [2, 1]))
print(union([1, 2, 3], [3, 2, 1]))
print(union([1, 2, 3], [3, 2, 4]))
print(union([1, 2, 3], [4, 5, 6]))