import math

def phuongtrinhbac2():
  a = float(input("a: "));
  b = float(input("b: "));
  c = float(input("b: "));
  return a,b,c;

def giai(a,b,c):
  if(a == 0):
    if(b == 0):
      if(c == 0):
        print("pt vô số nghiệm");
      else:
        print("pt vô nghiệm");
        pass
    else:
      x=-a/b;
      print("pt có nghiệm là: ", x);
      pass
    pass
  else:
    delta = math.pow(b,2)-4 * a * c;
    if(delta > 0):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        x = lambda a, b : a * b
        print("kiểu: ",type(x));
        print("Phuong trinh co hai nghiem phan biet:")
        print("x1 =", x1)
        print("x2 =", x2)
        pass
    elif delta == 0:
      x = -b / (2 * a)
      print("Phuong trinh co nghiem kep x =", str(x))
    else:
      print("Phuong trinh vo nghiem!")
  pass
def main():
  a, b, c = phuongtrinhbac2()
  giai(a, b, c)
  pass

if __name__ == "__main__":
  main();