import collections


def convert(s, numRows):
    ref = collections.defaultdict(list)
    count = 0
    direct = True
    if numRows == 1:
        return s
    for i in s:
        ref[count].append(i)
        if direct:
            count += 1
        else:
            count -= 1
        if count == 0:
            direct = True
        elif count == numRows - 1:
            direct = False
    ans = ''
    for i in range(numRows):
        ans += ''.join(ref[i])
    return ans

s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))
