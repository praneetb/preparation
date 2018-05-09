#
# Find kth element from Last in a linked list
# 

import linkedlist

class Node(object):
  def __init__(self, v):
    self.val = v
    self.next = None

  def SetNext(self, node):
    self.next = node

def FindKthElement(l, k):
  if k <= 0:
    return None

  n1 = n2 = l

  while(n2 and k > 0):
    n2 = n2.next
    k = k-1

  if n2 == None and k == 0:
    return n1
  
  if n2 == None:
    return None

  while (n2):
    n2 = n2.next
    n1 = n1.next

  return n1


def main():
  print("Find Kth element from last")
  _list = linkedlist.create_list(10, 10)
  linkedlist.print_list(_list)

  for i in range(13):
    res = FindKthElement(_list, i)
    if res:
      value = res.value
    else:
      value = -1
    print("\t%d from last: %d" %(i, value))

if __name__ == '__main__':
  main()
