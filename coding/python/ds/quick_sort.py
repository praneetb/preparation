#
# Quick Sort
#

import random

LIST_SIZE = 20


class QuickSort():
  def __init__(self, list):
    self._list = list

  def _partition(self, _list, low, high):
    pivot = low
    i = low+1
    j = high

    while True:
      while _list[pivot] >= _list[i]:
        if i == high:
          break
        i += 1
      while _list[pivot] < _list[j]:
        if j == low:
          break
        j -= 1
      if i >=  j:
        break

      # swap positions i and j
      tmp = _list[i]
      _list[i] = _list[j]
      _list[j] = tmp

    # swap pivot with j
    tmp = _list[pivot]
    _list[pivot] = _list[j]
    _list[j] = tmp

    return j

  def _sort(self, low, high):
    if low >= high:
      return

    ret = self._partition(self._list, low, high)
    self._sort(low, ret-1)
    self._sort(ret+1, high)

  def sort(self):
    self._sort(0, len(self._list)-1)

  def print_list(self):
    print self._list

def main():
  _list = [random.randint(0, 100) for i in range(0, LIST_SIZE)]
  qs = QuickSort(_list)
  qs.print_list()
  qs.sort()
  qs.print_list()

if __name__ == '__main__':
  main()

