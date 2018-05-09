# Linked list helpers

import random

class Node(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def create_list(sz, r):
  # generate random numbers
  _list = [random.randint(0, r) for i in range(0, sz)]

  
  head = Node(_list[0])
  pn = head
  for idx in range(1, len(_list)):
    n = Node(_list[idx])
    pn.next = n
    pn = n

  return head

def print_list(head):
  _list = []
  while (head):
    _list.append(head.value)
    head = head.next
  print _list
  return _list

def main():
  h =  create_list(10, 5)
  print_list(h)

if __name__ == '__main__':
  main()
