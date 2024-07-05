G = []
P = []

def Split(string):
    parts = string.split();
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    return a, b, c

def Init(path, G):
    with open(path, 'r') as f:
        string = f.readline().replace('\t', ' ')
        n, a, z = Split(string.replace('\t', ' '));
        for i in range(n + 1):
            G.append([0] * (n + 1))
        while True:
            string = f.readline()
            if not string:
                break
            string = string.replace('\t', ' ')
            i, j, x = Split(string.replace('\t', ' '));
            G[i][j] = G[j][i] = x
    return n, a, z

def Check(M, n, u):
    for i in range(1, n + 1):
        if M[i] == u:
            return True
    return False

def viewMatrix(G, n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(f"{G[i][j]} ", end='')
        print()

def Breadth_First_Search(G, n, s, g, P):
    Open = [0] * (n + 3)
    Close = [0] * (n + 3)
    P.extend([0] * (n + 3))
    front = 1
    rear = 1
    Open[rear] = s
    P[s] = s
    
    while front <= rear:
        u = Open[front]
        front += 1
        if u == g:
            return True
        for v in range(1, n + 1):
            if G[u][v] != 0 and not Check(Open, n, v) and not Check(Close, n, v):
                rear += 1
                Open[rear] = v
                P[v] = u
        Close[u] = u
    return False

def Print(P, n, s, g):
    Path = [0] * (n + 1)
    print(f"\nĐƯỜNG ĐI TỪ {s} ĐẾN {g} LÀ\n", end=' ')
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
            print(f"{Path[i]} => ", end=' ');
        else:
            print(f"{Path[i]}", end=' ');

def main():
    n, s, g = Init("graph5.inp", G)
    if Breadth_First_Search(G, n, s, g, P):
        Print(P, n, s, g);
    else:
        print("No path found.");

if __name__ == "__main__":
    main();