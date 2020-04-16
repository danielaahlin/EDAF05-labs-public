import sys
import numpy as np

def prim(G, r, N):
    T = []
    Q = [i + 1 for i in range(N) if (i+1 != r)]
    while Q:
        print(Q)
        edges = [e for e in G if (e[0] not in Q and e[1] in Q)] #  or e[0] in Q and e[1] not in Q
        # print(edges)
        weights = [G[e] for e in edges]
        u, v = edges[np.argmin(weights)]
        # print('({}, {})'.format(u, v))
        if u not in Q:
            Q.pop(Q.index(v))
        else:
            Q.pop(Q.index(u))
        T.append((u,v))
        print(T)
    return T


def kruskal(G):
    pass

if __name__ == "__main__":
    lines = sys.stdin
    data = lines.read().split('\n')
    N, M = map(int, data[0].split())
    graph = {}
    for d in data[1:len(data)-1]:
        d = d.split()
        graph[(int(d[0]), int(d[1]))] = int(d[2])
    # print(graph)

    tree = prim(graph, 1, N)
    weight = sum([graph[e] for e in tree])
    print(weight)