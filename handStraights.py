def isNStraightHand(hand, W):
    if len(hand) % W != 0:
        return False
    hand.sort(reverse = False)
    lib = dict()
    for x in hand:
        if x not in lib:
            lib[x] = 1
        else:
            lib[x] += 1
    for item in lib.keys():
        while lib[item] > 0:
            for i in range(W):
                if item+i not in lib:
                    return False
                if lib[item+i] > 0:
                    lib[item+i] -= 1
                else:
                    return False

    return True

hand = [1,2,3,6,2,3,4,7,8]
W = 3
print(isNStraightHand(hand, W))

