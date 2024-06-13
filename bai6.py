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

def selectionSort(K, n):
  for i in range(n):
    for j in range(i + 1, n):
      if int(K[i]) > int(K[j]): 
        flag = K[i];
        K[i] = K[j];
        K[j] = flag;
  return K;

def main():
  global M;
  # n = int(input("a= "))
  n=5
  CreateArr(M, n)
  ViewArr(M, n)
  tong = SumArr(M, n)
  print("Tong cac phan tu trong mang: ", tong)
  tong_le = Sumle(M, n)
  print("Tong cac phan tu le trong mang: ", tong_le)
  M_sorted = selectionSort(M, n)
  print("Mang sau khi sap xep: ")
  ViewArr(M_sorted, n)
  pass
if __name__ == "__main__":
  main();