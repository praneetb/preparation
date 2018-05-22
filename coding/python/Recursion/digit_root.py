# Digit Root
# 1734 = 1+7+3+4 = 15 = 6

def digit_sum(n):
  if n <= 9:
    return n
  return digit_sum(n%10 + digit_sum(n/10))

def main():
  number = input("Enter number :")
  result = digit_sum(number)
  print("Number %d digit sum is %d" %(number, result))

if __name__ == '__main__':
  main()


