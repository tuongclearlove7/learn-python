import math

G = []
P = []
const = 10

def CreateQ(Open):
    for i in range(const):
        Open.append([])
        for j in range(3): 
            Open[i].append(0)
            
def EmptyQ(Open):
    return len(Open) - Open.count(Open[0]) == 0

def AddQ(Open, n, g_cost, h_cost, index):
    f_cost = g_cost + h_cost
    n = n + 1
    Open[n][0] = f_cost
    Open[n][1] = index
    Open[n][2] = g_cost  
    i = n
    while i > 1:
        j = int(i / 2)
        if Open[i][0] < Open[j][0]:
            temp = Open[i]
            Open[i] = Open[j]
            Open[j] = temp
        i = j
    return n

def RemoveQ(Open):
    f_cost = Open[1][0]
    index = Open[1][1]
    g_cost = Open[1][2]
    n = len(Open) - Open.count(Open[0])
    Open[1][0] = Open[n][0]
    Open[1][1] = Open[n][1]
    Open[1][2] = Open[n][2]
    Open[n][0] = 0; Open[n][1] = 0; Open[n][2] = 0
    n = n - 1; i = 1
    while i <= int(n / 2):
        j = i * 2
        if j < n:
            if Open[j][0] > Open[j + 1][0]:
                j = j + 1
            if Open[i][0] > Open[j][0]:
                Open[i], Open[j] = Open[j], Open[i]
        else:
            if Open[i][0] > Open[j][0]:
                Open[i], Open[j] = Open[j], Open[i]
        i = i + 1
    return f_cost, index, g_cost, n

def Split(string):
    parts = string.split()
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    return a, b, c

def Init(path, G):
    with open(path, 'r') as f:
        string = f.readline().strip()
        n, a, z = Split(string)
        for i in range(n + 1):
            G.append([0] * (n + 1))
        while True:
            string = f.readline()
            if not string:
                break
            i, j, x = Split(string.strip().replace('\t', ' '))
            G[i][j] = G[j][i] = x
    return n, a, z

def heuristic(node, goal):
    return abs(node - goal)

def Algorithm_for_tree(G, P, n, s, g):
    resul = 0
    Close = []
    o = []
    for i in range(const):
        Close.append(0)
        o.append(0)
        P.append(0)
    Open = []
    CreateQ(Open)
    h_cost = heuristic(s, g)
    m = AddQ(Open, 0, resul, h_cost, s)
    o[s] = 1
    P[s] = s
    while not EmptyQ(Open):
        f_cost, u, g_cost, m = RemoveQ(Open)
        if u == g:
            resul = g_cost
            break
        for v in range(1, n + 1):
            if G[u][v] != 0 and o[v] == 0 and Close[v] == 0:
                g_cost_new = g_cost + G[u][v]
                h_cost_new = heuristic(v, g)
                m = AddQ(Open, m, g_cost_new, h_cost_new, v)
                o[v] = 1
                P[v] = u
        Close[u] = 1
        o[u] = 0
    return resul

def Print(P, n, s, g):
    Path = [0] * (n + 1)
    print("\nĐường đi từ nút %d đến nút %d là:" % (s, g))
    Path[0] = g
    i = P[g]
    k = 1
    while i != s:
        Path[k] = i
        k += 1
        i = P[i]
    Path[k] = s
    for j in range(k + 1):
        i = k - j
        if i > 0:
            print("%d => " % Path[i], end=' ')
        else:
            print("%d " % Path[i], end=' ')

def main():
    n, s, g = Init("cay.inp", G)
    resul = Algorithm_for_tree(G, P, n, s, g)
    Print(P, n, s, g)
    print("\nresul: %d" % resul, end='\n')

if __name__ == "__main__":
    main()



# 8	8 7
# 1	8 2   
# 2	4 4
# 2	5 2
# 2	8 3
# 3	6 7
# 3 8 4
# 5	7 5