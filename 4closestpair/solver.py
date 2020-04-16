import sys
import numpy as np

def closest_points(Px, Py, n):
    print('CLOSEST')
    dist = 1e10
    for i in range(n):
        print(i)
        for j in range(i + 1, n):
            # print('i: {}, j: {}'.format(i, j))
            dist = min(dist, np.sqrt( (Px[i] - Px[j])**2 + (Py[i] - Py[j])**2 ))
            # print(dist)
    return dist

if __name__ == "__main__":
    lines = sys.stdin
    data = lines.read().split('\n')
    n = int(data[0])
    coords = [(int(d.split()[0]), int(d.split()[1])) for d in data[1:len(data)-1]]
    # print(n)
    # print(coords)

    mid_point = float(sum(x[0] for x in coords) / len(coords))
    # print(mid_point)

    L_idx = []
    R_idx = []

    for idx, point in enumerate(coords):
        x = float(point[0])
        if x < mid_point:
            L_idx.append(idx)
        else:
            R_idx.append(idx)
    # print(L_idx)
    # print(R_idx)
    Rp = [coords[i] for i in R_idx]
    Lp = [coords[i] for i in L_idx]
    Rx = [p[0] for p in Rp]
    Ry = [p[1] for p in Rp]
    Lx = [p[0] for p in Lp]
    Ly = [p[1] for p in Lp]
    # print(Lp)
    # print(Rp)
    # print('---')
    # print('Right')
    d_r = closest_points(Rx, Ry, len(Rp))
    # print('Left')
    d_l = closest_points(Lx, Ly, len(Lp))
    sigma = min(d_l, d_r)
    # print(sigma)
    # print(mid_point)
    
    Sp = [p for p in coords if (p[0] <= (mid_point + sigma) and p[0] >= (mid_point - sigma))]
    d_s = 1e10 
    if len(Sp) > 1:
        Sx = [p[0] for p in Sp]
        Sy = [p[1] for p in Sp]
        d_s = closest_points(Sx, Sy, len(Sp))
    
    closest = np.round(min(sigma, d_s), decimals=6)
    print('%.6f' % closest)