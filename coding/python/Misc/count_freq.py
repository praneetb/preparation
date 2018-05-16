#
# Given an unsorted array of n integers which can contain
# integers from 1 to n. Some elements can be repeated
# multiple times and some other elements can be absent
# from the array. Count frequency of all elements that
# are present and print the missing elements.
#

import random

class CountNumbers():
  def __init__(self, num):
    self.num = num
    self.ll = [random.randint(1, num) for _ in range(num)]
    print self.ll

  def count_simple(self):
    self.cl = [0 for _ in range(self.num)]
    for n in self.ll:
      self.cl[n-1] += 1

  def count_hard(self):
    idx = 0
    while idx < self.num:
      num = self.ll[idx]

      if num < 0:
        # element is processed
        idx += 1
        continue

      if self.ll[num-1] > 0:
        self.ll[idx] = self.ll[num-1]
        self.ll[num-1] = -1
      else:
        self.ll[num-1] += -1
        self.ll[idx] = 0
        idx += 1
      
  def print_simple(self):
    return self.cl

  def print_hard(self):
    ll = [-x for x in self.ll]
    return ll


def main():
  num = input("Enter number :")
  cn = CountNumbers(num)
  cn.count_simple()
  print cn.print_simple()
  cn.count_hard()
  print cn.print_hard()
  
if __name__ == '__main__':
  main()
