#
# Given a number x, determine whether the given number is
# Armstrong number or not. A positive integer of n digits
# is called an Armstrong number of order n
# (order is number of digits) if.
#
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
#

import sys

def get_arm(ll):
  arm = 0
  ndig = len(ll)
  for n in range(ndig):
    arm += pow(int(ll[n]), ndig)

  return arm

def NArmstrong(nth):
  count = 0
  for num in xrange(1, sys.maxint):
    ll = list(str(num))
    res = get_arm(ll)
    if res == num:
      count += 1
      if count == nth:
        return res

def main():
  print "Armstrong Number"
  nth = input("Enter nth number: ")
  print "%d armstong number is %d" %(nth, NArmstrong(nth))
  #print get_arm(list(str(nth)))

if __name__ == '__main__':
  main()
