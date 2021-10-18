import math

import random
def distance(p1, p2):
    return math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
                minNames = (p[i][0], p[j][0])

    return mindist, minNames

def strip_closest(P,d):
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[2])
    minNames = ("", "")
    
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(p[i][2] - p[j][2]) < d_min:
                dij = distance(P[i], p[j])
                if dij < d_min:
                    d_min = dij
                    minNames = (p[i][0], p[j][0])
            else:
                break
    return d_min, minNames

def closest_pair_dist(P ,n):
    if n <=3:
        return closest_pair(P)
    
    mid = n // 2
    mid_x = p[mid][1]

    d1, minNames = closest_pair_dist(P[:mid], mid)
    dr, minNames2 = closest_pair_dist(P[mid:], n - mid)
    d = min(d1, dr)

    if d != d1:
        minNames = minNames2
    
    Pm = []

    for i in range(n):
        if abs(P[i][1] - mid_x) < d: # 여기도 고쳐야됨
            Pm.append(P[i])
    ds, minNames2 = strip_closest(Pm, d)
    
    if d <= ds:
        return d, minNames
    else:
        return ds, minNames2
p = []
for i in range(20):
    x, y = random.randint(1, 100), random.randint(1, 100)
    p.append((chr(65 + i), x, y))
#p = [("A", 2,3), ("B", 12,30),("C", 40,50),("D", 5,1),("E", 12,10),("F", 3,4)]
p.sort(key = lambda k:k[1])
print(p)
d, minNames = closest_pair_dist(p, len(p))
print(" 가장 가까운 두 점의 거리 : ", d)
print(" 두 쌍 : {} {}".format(minNames[0], minNames[1]))