def inputN():
  n = int(input("n: "))
  n2 = int(input("n: "))
  n3 = int(input("n: "))
  return n, n2, n3;
def soLonNhat(n, n2, n3):
  maxvalue = n;
  if maxvalue < n2:
    maxvalue = n2;
  if maxvalue < n3:
    maxvalue = n3;
  return maxvalue;

def main():
  n,n2,n3 = inputN();
  max_ = max(n, n2, n3);
  print ("Số lớn nhất: ", max_);
  pass
if __name__ == "__main__":
  main();


