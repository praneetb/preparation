#
# Spiral Matrix
# Traverse matrix spirally
#  [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
#

from pprint import pprint

matrix = [
  [ 1,  2,  3,  4,  5  ],
  [ 6,  7,  8,  9,  10 ],
  [ 11, 12, 13, 14, 15 ],
  [ 16, 17, 18, 19, 20 ],
  [ 21, 22, 23, 24, 25 ],
]

result = []

def print_outer_matrix(matrix, rmi, rma, cmi, cma):
  i = cmi
  while i < cma:
     result.append(matrix[rmi][i])
     i += 1

  i = rmi+1
  while i < rma:
     result.append(matrix[i][cma-1])
     i += 1

  i = cma-2
  while i >= cmi:
     result.append(matrix[rma-1][i])
     i -= 1

  i = rma-2
  while i >= rmi+1:
     result.append(matrix[i][cmi])
     i -= 1

def traverse_matrix(matrix, rmi, rma, cmi, cma):
  for i in range(len(matrix)):
    pprint(matrix[i])

  while ((rmi < rma) and (cmi < cma)):
    print_outer_matrix(matrix, rmi, rma, cmi, cma)
    rmi += 1
    rma -= 1
    cmi += 1
    cma -= 1

def main():
   row_min = 0
   row_max = len(matrix)
   col_min = 0
   col_max = len(matrix[0])
   traverse_matrix(matrix, row_min, row_max, col_min, col_max)
   print(result)

if __name__ == '__main__':
  main()
