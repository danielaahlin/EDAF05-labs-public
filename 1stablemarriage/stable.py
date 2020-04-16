import sys
import operator

def sort_data(std_in):
    women = []
    men = []

    # with open(path, 'r') as file:
    i = 0
    for f in std_in:
        data = f.split()
        if len(data) == 1:
            N = int(data[0])
            # print(N)
        else:
            if i >= N * 2:
                break
            else:
                i += 1
            gender_id = int(data[0])
            pref_list = [int(i) for i in data[1:]]
            obj = {'id': gender_id, 'pref_list' : pref_list}
            is_woman = True
            for w in women:
                if w['id'] == gender_id:
                    is_woman = False
                    break
            if is_woman:
                women.append({**obj, 'partner' : {}})
            else:
                men.append({**obj, 'proposed' : []})

    return N, women, men

def prefer(w, m, mw):
    w_prefs = w['pref_list']
    for i in w_prefs:
        if m['id'] == i:
            return True
        elif mw['id'] == i:
            return False
    return False

def remove_pair(mw, w, partners):
    i = 0
    for p in partners:
        if p[0] == mw['id']:
            partners.pop(i)
        i += 1
    return partners

if __name__ == "__main__":
    # print(sys.stdin)
    std_in = sys.stdin
    # for line in std_in:
    #     print(line)
    # if len(sys.argv) < 2:
    #     print('Wrong amount of input')
    #     exit()

    # path = sys.argv[1]
    N, women, men = sort_data(std_in)
    women = sorted(women, key=lambda i : i['id'] )
    men = sorted(men, key= lambda i : i['id'])
    partners = []
    p = [m for m in men]
    # print(men)
    # print(women)
    while len(p) > 0:
        # print(partners)
        # print(p)
        m = p.pop(0)
        if m['proposed']:
            for w_i in m['pref_list']:
                if w_i not in m['proposed']:
                    w_idx = w_i
                    break
        else:
            w_idx = m['pref_list'][0]
        w = women[w_idx - 1]
        # print(w)
        # print(m)
        m['proposed'].append(w['id'])
        if w['partner'] == {}:
            w['partner'] = m
            partners.append((m['id'], w['id']))
        elif prefer(w, m, w['partner']):
            mw = w['partner']
            partners = remove_pair(mw, w, partners)
            partners.append((m['id'], w['id']))
            p.append(mw)
            w['partner'] = m
            # m['proposed'].append(w['id'])
        else:
            p.append(m)
    partners.sort(key=operator.itemgetter(1))
    # print(partners)
    for p in partners:
        # print(p)
        print(p[0])