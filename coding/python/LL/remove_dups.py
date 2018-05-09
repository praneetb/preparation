# remove duplicate from linked list

import linkedlist

def rem_dups(head):
  if head == None or head.next == None:
    return head

  #import pdb; pdb.set_trace()
  hash_list = {}
  phead = head
  hash_list[head.value] = 1
  pphead = head.next
  while (pphead):
    if hash_list.get(pphead.value) == None:
      hash_list[pphead.value] = 1
      phead = pphead
    else:
      phead.next = pphead.next
    pphead = pphead.next
  print len(hash_list), len(linkedlist.print_list(head))
  return head 

def main():
  head = linkedlist.create_list(20, 10)
  linkedlist.print_list(head)
  new_list = rem_dups(head)
  linkedlist.print_list(new_list)

if __name__ == '__main__':
  main()
