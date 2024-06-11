def inputN():
  n = int(input("n: "))
  return n;
def giaithua(n):
  s = 1;
  for i in range(1, n+1):
    s=s*i;
    pass
  return s;
def main():
  n = inputN()
  print("Kết quả: ",n,"! = ",giaithua(n));
  pass
if __name__ == "__main__":
  main();