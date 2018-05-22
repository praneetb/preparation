# number to power of k
# Write code to calculate n to power of k using recursion

def calc_power(n, k):
  if k == 0:
    return 1
  return n * calc_power(n, k-1)

def main():
  number = input("Enter number :")
  power = input("Enter power :")
  result = calc_power(number, power)
  print("Number %d^%d = %d" %(number, power, result))

if __name__ == '__main__':
  main()

