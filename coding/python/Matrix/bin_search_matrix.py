#
# search a sorted matrix
#

from pprint import pprint

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

def search_number(matrix, num):
  found = 0

  row = len(matrix)
  col = len(matrix[0])

  print "row=%d, col=%d" %(row,col)
  first = 0
  last = (row*col)-1

  while (first <= last):
    mid = (first+last)/2
    c_row = mid/col
    c_col = mid%col
    print "f-%d, l-%d, m-%d, cr-%d, cl-%d" %(first, last, mid, c_row, c_col)
    if matrix[c_row][c_col] == num:
      found = 1
      break
    elif (num < matrix[c_row][c_col]):
      last = mid-1
    elif (num > matrix[c_row][c_col]):
      first = mid+1

  return found

def main():
  pprint(matrix)
  num = int(raw_input('Enter number to search:'))
  found = search_number(matrix, num)
  if found:
    print "Number %d was Found" % (num)
  else:
    print "Number %d was Not Found" % (num)

if __name__ == '__main__':
    main()
