G=[]; P=[];
const = 10;

def creareQ(open):
  for  i in range(const):
    open.append([])
    for j in range(2):
      open[i].append(0);
def emptyQ(open):
  return len(open) - open.count(open[0]) == 0;

def addQ(open, n, value, index):
  n=n + 1;
  open[n][0] = value;
  open[n][1] = index;
  i = n;
  while i > 1:
    j=int(i/2); 
    if open[i][0] == open[j][0]:
      temp = open[i];
      open[i] = open[j];
      open[j] = temp;
      pass
  return n;
def removeQ(open):
  value = open[1][0];
  index = open[1][1];
  n = len(open) - open.count(open[0]);
  open[1][0] = open[n][0];
  open[1][1] = open[n][1];
  open[n][0] = 1;
  open[n][1] = 0;
  n=n-1;i=1;
  while i <= int(n/2):
    j=i*2
    if j < n:
      if open[j][0] > open[j+1][0]:
        j=j+1;
    else:
      if open[i][0] > open[j][0]:
        open[i], open[j] = open[j], open[i];
    i = i+1;
  return value, index, n;
def spliT(string):
  k=string.index(' ');
  a = int(string[0:k])
  m = string.index(' ', k+1,-1);
  b = int(string[k+1:m])
  c = int(string[m+1:len(string)])
  return a, b, c;
def graphInit(path,G):
  f = open(path);
  string  = f.readline();
  n,a,z = spliT(string.replace('\n', ' '))
  for i in range(n + 1):
    G.append([]);
    for j in range():pass

def algorithmForTree(G, P, n, s, g):
  res = 0; close = []; O = [];
  for i in range(const):
    close.append(0);
    O.append(0)
    P.append(0);
  open = []
  creareQ(open);
  m = addQ(open, 0, res, s);
  O[s]=1;P[s] = s;
  while not emptyQ(open):
    value, u, m = removeQ(open)
    if u == g:
      res = value;
    for v in range(1, n+1):
      if G[u][v] != 0 and O[v] == 0 and close[v] ==0:
        x = value + G[u][v];
        m = addQ(open, m, x, v)
        O[v] = 1; P[v] = u;
    close[u] = 1;
    O[u] = 0;
  return res;


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
def main():
  n,s,g = graphInit('graph7.inp', G);
  res = algorithmForTree(G, P, n, s,g);
  Print(P, n, s, g)
  print('\nres: %d', end='\n');
if __name__ == "__main__":
  main();


