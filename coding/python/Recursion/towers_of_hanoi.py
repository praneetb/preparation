#
# Towers of Hanoi
#

def usr_input(s, e, t):
  ch = ""
  while ch != "c" and ch != "C":
    print s
    print e
    print t
    ch = raw_input("Enter 'c' to continue: ")

def move_one(l1, l2, l3):
  usr_input(l1, l2, l3)
  l2.append(l1.pop())
  usr_input(l1, l2, l3)

def permute(h, start, end, tmp):
  if h == 1:
    move_one(start, end, tmp)
    return

  permute(h-1, start, tmp, end)
  move_one(start, end, tmp)
  permute(h-1, tmp, end, start)

def main():
  height = input("Enter height of towers :")
  la = [height-i for i in range(0, height)]
  la.insert(0, 'start')
  lb = ['tmp']
  lc = ['end']
  print la
  print "Start ...."
  permute(height, la, lc, lb)
  print la
  print lc

if __name__ == '__main__':
  main()





