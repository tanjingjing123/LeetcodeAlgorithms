def shortestWay(source, target):
    i, m = 0, 1
    for c in target:
        i = source.find(c, i)
        if i == -1:
            i = source.find(c)
            m += 1
            if i == -1:
                return -1
        i += 1

    return m

source = "xyzxadde"
target = "xzyaedxz"
print(shortestWay(source,target))