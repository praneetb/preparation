#
# find number of islands in a 2D graph
#

island = [
  [ 1, 0, 0, 1, 0  ],
  [ 0, 1, 0, 1, 0  ],
  [ 1, 0, 1, 0, 0  ],
  [ 0, 1, 0, 1, 1  ],
]

def check_around(island, i, j):
  m = len(island)
  n = len(island[0])

  #import pdb; pdb.set_trace()
  if i < 0 or i >= m or j < 0 or j >= n or not island[i][j] is 1:
    return

  #mark the place visited
  island[i][j] = 'V'

  check_around(island, i-1, j)
  check_around(island, i+1, j)
  check_around(island, i, j-1)
  check_around(island, i, j+1)
  # uncomment below for any conenction horizontal/vertical, diagonal
  #check_around(island, i-1, j-1)
  #check_around(island, i+1, j-1)
  #check_around(island, i-1, j+1)
  #check_around(island, i+1, j+1)

def num_islands(island):
  count = 0
  if island is None or len(island) is 0 or len(island) is 0:
      return 0
  m = len(island)
  n = len(island[0])

  for i in range(m):
    for j in range(n):
      if island[i][j] is 1:
        count += 1   
        check_around(island, i, j)
  return count

def main():
  count = num_islands(island)
  print "Number of Islands = %d" %(count)
  print "####"
  print island
  print "####"

if __name__ == '__main__':
    main()
