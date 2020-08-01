def maxLength(arr):
    if len(arr) == 1:
        return len(arr[0])

    else:
        unique_ele = ['']
        maxlen = 0
        for i in range(len(arr)):
            for j in range(len(unique_ele)):
                x = arr[i] + unique_ele[j]
                if len(x) == len(set(x)):
                    unique_ele.append(x)
                    maxlen = max(maxlen, len(x))
                else:
                    continue
    return maxlen


arr = ["un","iq","ue"]
print(maxLength(arr))