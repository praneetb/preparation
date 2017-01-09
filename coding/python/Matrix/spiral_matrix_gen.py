#
# Spiral Matrix
#  Given an integer n, generate a square matrix filled
#  with elements from 1 to n2 in spiral order.
#  For example, given n = 4,
#  [
#    [1,   2,  3, 4], 
#    [12, 13, 14, 5], 
#    [11, 16, 15, 6], 
#    [10,  9,  8, 7]
#  ]
#

from pprint import pprint

def build_outer_matrix(matrix, rmi, rma, cmi, cma):
  global counter
  i = cmi
  while i < cma:
     counter += 1
     matrix[rmi][i] = counter
     i += 1

  i = rmi+1
  while i < rma:
     counter += 1
     matrix[i][cma-1] = counter
     i += 1

  i = cma-2
  while i >= cmi:
     counter += 1
     matrix[rma-1][i] = counter
     i -= 1

  i = rma-2
  while i >= rmi+1:
     counter += 1
     matrix[i][cmi] = counter
     i -= 1

def traverse_matrix(matrix, rmi, rma, cmi, cma):
  while ((rmi < rma) and (cmi < cma)):
    build_outer_matrix(matrix, rmi, rma, cmi, cma)
    rmi += 1
    rma -= 1
    cmi += 1
    cma -= 1

def main():
  global dims
  global counter
  dims = int(raw_input('Enter num rows/columns:'))
  counter = 0

  matrix = [['#' for x in range(dims)] for y in range(dims)]

  row_min = 0
  row_max = len(matrix)
  col_min = 0
  col_max = len(matrix[0])

  traverse_matrix(matrix, row_min, row_max, col_min, col_max)
  for i in range(len(matrix)):
    pprint(matrix[i])


if __name__ == '__main__':
  main()
