# number to power of k
# Write code to calculate n to power of k using recursion

def int_2_str(n):
  if n <= 9:
    return str(n)
  return int_2_str(n/10) + str(n%10) 

def main():
  n = input("Enter number :")
  s = int_2_str(n)
  print "String: " + s

if __name__ == '__main__':
  main()


