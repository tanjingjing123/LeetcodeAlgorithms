import collections
def findMaxContiguous(nums):
    # visualize nums as a grpah. if found 0 goes up, if 1 goes down
    g = 0  # initial position in the graph is zero, g points toward position in the graph
    longest = 0  # keeps track of longest distance between same points in graph
    hm = {0: -1}  # position 0 at graph is first found at index -1/ before start

    for i, n in enumerate(nums):
        if n == 0:
            g += 1
        else:
            g -= 1
        if g in hm.keys():
            longest = max(longest, i - hm[g])
        else:
            hm[g] = i  # g first found at index i

    return longest

nums = [0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0]
print(findMaxContiguous(nums))


