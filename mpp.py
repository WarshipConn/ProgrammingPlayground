import random
items = ["A", "B", "C", "D", "E"]

# stores derangements in a map x -> D_x
cache = {}

def derangement(x):
    if x < 0:
        return -1
    if x in cache:
        return cache[x]

    ans = 0
    if x == 0:
        ans = 1
    elif x == 1:
        ans = 0
    else:
        ans = (x-1) * (derangement(x-1) + derangement(x-2))

    cache[x] = ans
    return ans

def probabilityPair(x):
    return derangement(x-2) / ((x-1) * derangement(x-1) + derangement(x-2))

DEBUG_TRACE = False

def mpp(items):
    # list with elements which swap in place
    remaining = list(items)
    key = list(items)
    # all indicies on left of cur (inclusive), are already paired
    cur = 0

    map = {}

    while cur < len(remaining):
        j = random.randint(cur+1, len(remaining)-1)

        des = random.random()
        threshold = probabilityPair(len(remaining) - cur)

        if DEBUG_TRACE:
            print(threshold)

        if des < threshold:
            # pair
            #print(remaining[cur], remaining[j])
            map[key[cur]] = remaining[j]
            map[key[j]] = remaining[cur]
            remaining[cur+1], remaining[j] = remaining[j], remaining[cur+1]
            cur += 2
        else:
            # single 
            map[key[cur]] = remaining[j]
            remaining[cur], remaining[j] = remaining[j], remaining[cur]
            cur += 1

        if DEBUG_TRACE:
            print(cur, j, remaining, map)

    if DEBUG_TRACE:
        print(remaining)
    
    return map

print(mpp(items))