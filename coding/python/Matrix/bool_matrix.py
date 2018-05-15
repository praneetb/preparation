#
# Given a boolean matrix mat[M][N] of size M X N,
# modify it such that if a matrix cell mat[i][j]
# is 1 (or true) then make all the cells of ith
# row and jth column as 1.
#

import random

def bool_matrix(matrix, r, c):
  rows = [0] * r
  cols = [0] * c

  for i in range(r):
    for j in range(c):
      if matrix[i][j] == 1:
        rows[i] = 1
        cols[j] = 1

  for i in range(r):
    for j in range(c):
      if rows[i] == 1 or cols[j] == 1:
        matrix[i][j] = 1

def main():
  # 5 rows , 6 columns
  r, c = 5,6
  matrix = [[random.randint(0,1) for _ in range(c)] for _ in range(r)]
  for i in range(r):
    print matrix[i]
  bool_matrix(matrix, r, c)
  print "Result:"
  for i in range(r):
    print matrix[i]
  

if __name__ == '__main__':
  main()
