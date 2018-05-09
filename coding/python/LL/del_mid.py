
# delete middle element of linked list

import linkedlist

def del_mid(_list):
  if _list == None or _list.next == None:
    return None

  #import pdb; pdb.set_trace()
  plist1 = _list
  plist2 = plist1.next
  while plist2 != None:
    plist2 = plist2.next
    if plist2:
      plist2 = plist2.next
      if plist2:
        plist1 = plist1.next

  plist1.next = plist1.next.next
  return _list
    

def main():
  _list = linkedlist.create_list(5, 10)
  linkedlist.print_list(_list)
  _list = del_mid(_list)
  linkedlist.print_list(_list)
if __name__ == '__main__':
  main()
