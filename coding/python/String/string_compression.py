# example:
#  aabbcccdeeee => a2b2c3d1e4
#

def compress(str0):
  l2 = [""] * len(str0) *2

  odx = -1
  ch = ""
  for idx in range(len(str0)):
    if ch != str0[idx]:
      odx += 1
      ch = str0[idx]
      l2[odx] = ch
      odx += 1
      count = 1
      l2[odx] = str(count)
    else:
      count += 1
      l2[odx] = str(count)
  
  return "".join(l2)

def main():
  string = raw_input("Enter string: ")
  print ("Compressed string is " + compress(string))

if __name__ == '__main__':
  main()
 
