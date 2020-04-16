import sys

def opt(i, j, sigma):
    if i == 0:
        return j * sigma
    elif j == 0:
        return i * sigma
    else:
        return max(allignments[chars[i]][chars[j]] + opt(i-1, j-1,sigma), 
                    sigma + opt(i, j-1, sigma),
                    sigma + opt(i-1, j, sigma))

if __name__ == "__main__":
    lines = sys.stdin
    data = lines.read().split('\n')
    print(data)
    chars = data[0].split()
    n = len(chars)
    costs = data[1:n+1]
    costs = [d.split() for d in costs]
    print(costs)
    Q = int(data[n+1])
    seq = data[n+2:n+2+Q]

    allignments = {}
    
    for idx, c in enumerate(chars):
        print(idx, c)
        allignments[c] = {chars[i] : int(costs[idx][i]) for i in range(n)}
    print(allignments)

    A = [['' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = opt(i, j, -4)
    print(A)