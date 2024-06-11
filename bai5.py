def inputN():
  n = int(input("n: "))
  n2 = int(input("n: "))
  return n, n2;

def UCLN(a, b):
  if a == 0 or b == 0:
    return a + b;
  min_value = min(a, b)
  n = 1
  for i in range(1, min_value + 1):
    if a % i == 0 and b % i == 0:
      n = i
  return n;
def main():
  n,n2 = inputN()
  u = UCLN(n, n2);
  print ("UCLN: ", u)
  pass
if __name__ == "__main__":
  main();