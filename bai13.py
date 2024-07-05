G = []
P = []
n = 0

def split(string):
    parts = string.split()
    if len(parts) != 3:
        raise ValueError("Input string must contain exactly three parts separated by spaces.")
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    return a, b, c

def Init(path, G):
    with open(path) as f:
        string = f.readline().strip()
        n, a, z = split(string.replace('\t', ''))
        for i in range(n + 1):
            G.append([0] * (n + 1))
        while True:
            string = f.readline().strip()
            if not string:
                break
            i, j, x = split(string.replace('\t', ''))
            G[i][j] = G[j][i] = x
    return n, a, z

def check(M, n, u):
    for i in range(1, n + 1):
        if M[i] == u:
            return True
    return False

def viewMatrix(G, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("%d " % G[i][j], end='')
        print()

def Depth_First_Search(G, P, n, s, g):
    open = []
    close = []
    for i in range(n + 3):
        open.append(0)
        close.append(0)
        P.append(0)
    top = 1
    open[top] = s
    P[s] = s
    while top > 0:
        u = open[top]
        top = top - 1
        if u == g:
            return 1
        for v in range(n, 0, -1):
            if G[u][v] != 0 and not check(open, n, v) and not check(close, n, v):
                top = top + 1
                open[top] = v
                P[v] = u
        close[u] = u
    return 0

def Print(P, n, s, g):
    path = []
    for i in range(0, n + 1):
        path.append(0)
    print("\nDuong di tu %d den %d la: " % (s, g), end='')
    path[0] = g
    i = P[g]
    k = 1
    while i != s:
        path[k] = i
        k = k + 1
        i = P[i]
    path[k] = s
    for j in range(0, k + 1):
        i = k - j
        if i > 0:
            print("%d --> " % path[i], end='')
        else:
            print("%d " % path[i], end='')
    return 0

def main():
    n, s, g = Init("graph6.inp", G)
    print("Xem ma tran G:", end='\n')
    viewMatrix(G, n)
    if Depth_First_Search(G, P, n, s, g):
        Print(P, n, s, g)
    else:
        print("Khong co duong di tu %d den %d" % (s, g))

if __name__ == "__main__":
    main()