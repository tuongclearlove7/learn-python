import time;


print("Hello world!");


name = "tuong";
print(name);

# a = int(input("a: "));
# amount = float(input("amount: "));

# print("a = ", a);
# print("amount = " + str(amount));

def phuongtrinhbacnhat():
  a = float(input("a: "));
  b = float(input("b: "));
  return a, b;
def giai(a, b):
  if(a == 0):
    if(b == 0):
      print("");
    else:
      print("vô số nghiệm");
      pass
  else:
    x = -a/b
    print("pt có nghiệm là: ",x);
    pass

def main():
  a, b = phuongtrinhbacnhat();
  giai(a,b);

if __name__ == "__main__":
    main();


# for i in range(10):
#   time.sleep(0.5)
#   print(i)






































