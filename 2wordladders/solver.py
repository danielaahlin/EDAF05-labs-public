import sys

def build_graph(words):
    graph = {w : [] for w in words}
    for w in words:
        for w2 in words:
            if w != w2:
                score = compare_words(w, w2)
                if score == len(w) - 1:
                    graph[w].append(w2)
    return graph

def compare_words(word1, word2):
    comp_score = 0
    comp_word = [l for l in word2]
    for letter in word1[1:]:
        for idx, letter2 in enumerate(comp_word):
            if letter == letter2:
                comp_word.pop(idx)
                comp_score += 1
                break
    return comp_score

def main(graph, match_words):
    
    # print(graph)
    for idx, m in enumerate(match_words):
        # print('---')
        # print(m)
        src, dest = m.split()
        visited = [src]
        added = 1
        length = 0
        printed = False
        # pred = ['' for _ in range(N)]

        if src == dest:
            print(length)
            # print('{}. {}'.format(idx, length))
            printed = True
            added = 0
        while added != 0:
            neighbors = list(set([g for v in visited for g in graph[v]]))
            # print(neighbors)
            added = 0

            if dest in neighbors:
                length += 1
                print(length)
                # print('{}. {}'.format(idx, length))
                printed = True
                break
            for n in neighbors:
                if n not in visited:
                    visited.append(n)
                    added += 1
            length += 1

            # print(visited)

        if not printed:
            print('Impossible')
            # print('{}. Impossible'.format(idx))

def bfs(graph, s, t):
    # print('--')
    # print(s)
    # print(t)
    visited = {w : 0 for w in graph}
    visited[s] = 1
    q = [s]
    if s == t:
        print(0)
        return
    while q:
        v = q.pop(0)
        for w in graph[v]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)
                pred[w] = v
                if w == t:
                    # print('Path found!')
                    path_tile = t
                    path = []
                    # print(pred)
                    while path_tile != s:
                        path.append(path_tile)
                        path_tile = pred[path_tile]
                    print(len(path))
                    return
    print('Impossible')

if __name__ == "__main__":
    lines = sys.stdin
    data = lines.read().split('\n')
    N, Q = map(int, data[0].split())
    words = data[1:N+1]
    match_words = data[N+1:N+1+Q]
    # print(data)
    # print(words)
    # print(match_words)
    graph = build_graph(words)

    # main(graph, match_words)

    for m in match_words:
        pred = {w : '' for w in graph}
        s, t = m.split()
        bfs(graph, s, t)