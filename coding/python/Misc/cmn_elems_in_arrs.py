# find all common elements in arrays
#
#

import random

class Common():
  def __init__(self, n):
    self.num = n
    self.lists = []
    self.all_common = []
    self.make_lists()

  def make_lists(self):
    for i in range(self.num):
      self.lists.append(sorted(set([random.randint(0,25)  for _ in range(0, random.randint(10,30))])))

  def print_lists(self):
    for i in range(self.num):
      print self.lists[i]

  def find_common(self):
    idxs = [0]*self.num
    lens = [len(self.lists[i]) for i in range(self.num)]
    while True:
      same = True
      min = 0
      for i in range(self.num-1):
        if self.lists[i][idxs[i]] == self.lists[i+1][idxs[i+1]]:
          continue
        if self.lists[i][idxs[i]] > self.lists[i+1][idxs[i+1]]:
          min = i+1
          same = False
          break
        if self.lists[i][idxs[i]] < self.lists[i+1][idxs[i+1]]:
          min = i
          same = False
          break

      if same:
        self.all_common.append(self.lists[min][idxs[min]])

      idxs[min] += 1
      if idxs[min] >= lens[min]:
        break

    return self.all_common
    

def main():
  num = input("Enter number of lists :")
  cmn = Common(num)
  cmn.print_lists()
  print "Result:"
  print cmn.find_common()

if __name__ == '__main__':
  main()
