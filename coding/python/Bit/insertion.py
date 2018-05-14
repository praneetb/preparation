#
# two 32 bit numbers M and N
# bit position i
# insert M into N such as M starts
# at i
#
# ex:
# Insert 101 into 1110111 at 2
# Result: 1010101
# 

def num_bits(x):
  count = 0
  while (x):
    count += 1
    x = x >> 1
  return count

def clear_bit(x, pos):
  mask = ~(1 << pos)
  return x&mask

def insert(N, M, pos):
  MMod = M << pos
  Mlen = num_bits(M)

  for i in range(pos, pos+Mlen):
    N = clear_bit(N, i)

  return N | MMod

def main():
  N = input("Enter a number : ")
  M = input("Enter a number : ")
  pos = input("Enter position to insert :")
  print "Insert " + str(bin(M)) + " into " + str(bin(N)) + " at " + str(pos)
  NewN = insert(N, M, pos)
  print "Result: " + str(bin(NewN))

if __name__ == '__main__':
  main()
