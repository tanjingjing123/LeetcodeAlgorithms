from collections import OrderedDict
def processQueries(queries, m):
    op = []
    a = [i for i in range(1, m + 1)]
    for val in queries:
        i = a.index(val)
        op.append(i)
        a.insert(0, a.pop(i))
    return op

queries = [7,5,5,8,3]
m = 8
print(processQueries(queries, m))
