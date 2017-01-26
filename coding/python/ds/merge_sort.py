#
# Merge Sort
# - Recursive Version
#

import random
import copy

LIST_SIZE = 20


class MergeSort:
  def __init__(self, numbers_list):
    self._list = numbers_list

  def _merge(self, l1, auxl1, low, mid, high):
    i = low
    j = mid+1
    k = low

    # copy to auxillary list
    for idx in range(low, high+1):
      auxl1[idx] = l1[idx]

    while k <= high:
      if i > mid:
        l1[k] = auxl1[j]
        j += 1
      elif j > high:
        l1[k] = auxl1[i]
        i += 1
      elif auxl1[i] < auxl1[j]:
        l1[k] = auxl1[i]
        i += 1
      else:
        l1[k] = auxl1[j]
        j += 1
      k += 1

  def _sort_recursive(self, l1, l2, l, h):
    if h <= l:
      return

    m = l+ (h - l)/2

    self._sort_recursive(l1, l2, l, m)
    self._sort_recursive(l1, l2, m+1, h)

    self._merge(l1, l2, l, m, h)

  def sort(self):
    low = 0
    high = len(self._list)-1

    list_copy = list(self._list)

    self._sort_recursive(self._list, list_copy, low, high)

  def print_list(self):
    print self._list

def main():
  _list = [random.randint(0, 100) for i in range(0, LIST_SIZE)]

  ms = MergeSort(_list)
  print 'UNSorted List is:'

  ms.print_list()
  ms.sort()
  print 'Sorted List is:'
  ms.print_list()

if __name__ == '__main__':
  main()
