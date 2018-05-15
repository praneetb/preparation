#
# Given a number n, print all primes smaller than or equal
# to n. It is also given that n is a small number.
#

class Prime():
  def __init__(self, n):
    self.num = n
    self.num_lists = []
    self.primes = []
    for i in range(n+1):
      self.num_lists.append(i)
    self.num_lists[0] = 0
    self.num_lists[1] = 0
    print self.num_lists

  def gen_primes(self):
    for i in range(self.num+1):
      if self.num_lists[i] == 0:
        # marked as 0, ignore
        continue
      m = 2*i
      while m < len(self.num_lists):
        self.num_lists[m] = 0
        m = m+i
    
    # primes are left in self.num_lists
    print self.num_lists
    self.primes = [self.num_lists[i] for i in range(self.num+1) if self.num_lists[i]]

  def get_primes(self):
    return self.primes
  
  
def main():
  n = input("Prime of: ")
  pr = Prime(n)
  pr.gen_primes()
  print pr.get_primes()

if __name__ == '__main__':
  main()
