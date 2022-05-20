def remove_all(x, xs):
    while xs != []:
        if x == xs[0]:
            xs.remove(x)
        else:
            if x in xs:
                xs.remove(x)
            else:
                return xs
    return xs        

#5 - 3 - (1)
def remove_duplicates(xs):
    if len(xs) >= 2:
        head = xs[0]
        return [head] + remove_duplicates(remove_all(head, xs))
    else:
        return xs
#5 - 3 - (2)
def remove_duplicates(xs):
    def loop(xs, total):
        if len(xs) >= 2:
            head = xs[0]
            return loop(remove_all(head, xs), total + [head])
        else:
            return total + xs
    return loop(xs, []) 

#5 - 3 - (3)
def remove_duplicates(xs):
    total = []
    while len(xs) >= 2:
        head = xs[0]
        total, xs = total + [head], xs + remove_all(head, xs)
    return total + xs

print(remove_duplicates([]))
print(remove_duplicates([1]))
print(remove_duplicates([1, 1]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([4, 2, 3, 2, 4, 3, 2, 1,]))

# no use remove_all def function 
def remove_duplicates(xs):
    if xs != []:
        if xs[0] in xs[1:]:
            return remove_duplicates(xs[1:])
        else:
            return [xs[0]] + remove_duplicates(xs[1:])
    else:
        return []
    
def remove_duplicates(xs):
    def loop(xs, zs):
        if xs != []:
            if xs[0] in xs[1:]:
                return loop(xs[1:], zs)
            else:
                return loop(xs[1:], zs + [xs[0]])
        else:
            return zs 
    return loop(xs, [])

def remove_duplicates(xs):
    total = []
    while xs != []:
        if xs[0] in xs[1:]:
            xs = xs[1:]
        else:
            total += [xs[0]]
            xs = xs[1:]
    return total  
