# Recursive Fibonacci
# 

def fibbo(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibbo(n-1) + fibbo(n-2)

def addn(n, x, y):
  if n == 0:
    return x
  if n == 1:
    return y
  return addn(n-1, y, x+y)

def fibbo_efficient(n):
  return addn(n, 0, 1)

def main():
  number = input("Enter number :")
  result = fibbo(number)
  print("Number %d has fibbonacci %d" %(number, result))
  result = fibbo_efficient(number)
  print("Number %d has fibbonacci %d" %(number, result))

if __name__ == '__main__':
  main()



