# GCD 
#
# The greatest common divisor (g.c.d.) of two nonnegative integers is the largest
# integer that divides evenly into both. In the third century B.C., the Greek
# mathematician Euclid discovered that the greatest common divisor of x and y can
# always be computed as follows:
# If x is evenly divisible by y, then y is the greatest common divisor.
# Otherwise, the greatest common divisor of x and y is always equal to the greatest
# common divisor of y and the remainder of x divided by y.

def gcd(n1, n2):
  rem = n1%n2
  if rem == 0:
    return n2
  return gcd(n2, rem)

def main():
  n1 = input("Enter number 1 :")
  n2 = input("Enter number 2 :")
  if n1 > n2:
    result = gcd(n1, n2)
  else:
    result = gcd(n2, n1)
  print("GCD of %d,%d = %d" %(n1, n2, result))

if __name__ == '__main__':
  main()


