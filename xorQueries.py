def xorQueries(arr, queries):
    ret = []
    for i in range(1, len(arr)):
        arr[i] ^= arr[i-1]

    for query in queries:
        if query[0] > 0:
            ret.append(arr[query[1]] ^ arr[query[0] - 1])
        else:
            ret.append(arr[query[1]])

    return ret

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr, queries))