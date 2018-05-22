# Iterative Fibonacci
# 

def fibbo(n):
  if n <= 2:
    return 1

  sum = 0
  p1 = 1
  p2 = 1
  for i in range(2, n):
    sum = p1 + p2
    p2 = p1
    p1 = sum

  return sum

def main():
  number = input("Enter number :")
  result = fibbo(number)
  print("Number %d has fibbonacci %d" %(number, result))

if __name__ == '__main__':
  main()


