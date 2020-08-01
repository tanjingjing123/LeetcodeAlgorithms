def minTotal(triangle):
    ans = [0] * len(triangle)
    for i, row in enumerate(triangle):
        for j in reversed(range(len(row))):
            if j == 0:
                ans[j] += row[j]
            elif j == len(triangle[i]) - 1:
                ans[j] = ans[j-1] + row[j]
            else:
                ans[j] = min(ans[j-1], ans[j]) + row[j]
    return min(ans)


triangle = [
     [2],
    [4,4],
   [3,5,4],
  [4,1,8,3]
]
print(minTotal(triangle))