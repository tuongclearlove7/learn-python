M=[]

def CreateArr(M, n):
  for i in range(n):
      M.append(int(input('Nhap so thu %d: ' % (i + 1))))

def ViewArr(M, n):
  for i in range(n):
      print("%d\t" % M[i], end=' ')
  print()

def SumArr(M, n):
  s = 0
  for i in range(n):
      s += int(M[i])
  return s

def Sumle(M, n):
  s = 0
  for i in range(n):
      if int(M[i]) % 2 != 0:
          s += int(M[i])
  return s

def sort(K, n):
  for i in range(n):
    for j in range(i + 1, n):
      if int(K[i]) > int(K[j]): 
        flag = K[i];
        K[i] = K[j];
        K[j] = flag;
  return K;

def main():
  global M;
  a = int(input("a= "))
  CreateArr(M, a)
  ViewArr(M, a)
  tong = SumArr(M, a)
  print("Tong cac phan tu trong mang: ", tong)
  tong_le = Sumle(M, a)
  print("Tong cac phan tu le trong mang: ", tong_le)
  M_sorted = sort(M, a)
  print("Mang sau khi sap xep: ")
  ViewArr(M_sorted, a)
  pass
if __name__ == "__main__":
  main();