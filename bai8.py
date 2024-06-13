G = []

def init_graph(path, G):
  with open(path) as f:
    n = int(f.readline(), base=10);
    for i in range(n + 1):
      G.append([])
      for j in range(n + 1):
        G[i].append(0)
    while True:
      string = f.readline()
      if not string:
        break;
      string = string.replace('\t', ' ')
      k = string.index(' ')
      i = int(string[0:k], base=10)
      m = string.index(' ', k + 1, -1)
      j = int(string[k + 1:m], base=10)
      x = int(string[m + 1:len(string)], base=10)
      G[i][j] = G[i][j] = x
  return n

def viewMatrix(G, n):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      print("%d" % G[i][j], end=' ')
    print()

def main():
  n = init_graph('graph.inp', G);
  print("Xem ma trận G", end='\n');
  viewMatrix(G, n);

if __name__ == "__main__":
  main()
