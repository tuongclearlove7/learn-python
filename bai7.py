A=[];B=[];C=[];D=[];
m=2; n=2;

def createMatrix(A, m, n, c):
  for i in range(m):
    A.append([]);
    for j in range(n):
      x=int(input("%c[%d][%d]= " %(c,i+1,j+1)))
      A[i].append(x);
def viewMatrix(A, m, n):
  for i in range(m):
    for j in range(n):
      print("[%d]" %A[i][j], end= ' ');
    print();
def sumMatrix(A, B, m, n):
  C=[];
  for i in range(m):
    C.append([]);
    for j in range(n):
      C.append(A[j][i] + B[j][i]);
  return C;
def multMatrix(A, B, m, n):
  D=[];
  for i in range(m):
    D.append([]);
    for j in range(n):
      x=0;
      for k in range(m):
        x=x+A[i][k]*B[k][j];
      D[i].append(x);
  return D;

def main():
  print("Tạo ma trận A: ", end='\n'); createMatrix(A, m, n, 'A');
  print("Xem ma trận A: ", end='\n'); viewMatrix(A, m, n);
  print("Tạo ma trận B: ", end='\n'); createMatrix(B, m, n, 'B');
  print("Xem ma trận B: ", end='\n'); viewMatrix(B, m, n);
  C = multMatrix(A, B, m, n);
  print("Xem ma trận C: ", end='\n'); viewMatrix(C, m, n);

if __name__ == "__main__":
  main();