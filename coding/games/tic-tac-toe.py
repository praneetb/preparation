#
# TIC TAC TOE
#

from pprint import pprint

#
# get row,col as input from player 1 or 2
#
def get_input(matrix, player):
  global num_plays
  valid_input = 0
  while not valid_input:
    row = int(raw_input('Player#%s-->(Enter ROW you wanna mark) ' %(player))) - 1 
    if row < 0 or row >= len(matrix):
      print "Invalid ROW value!!!"
      continue
    col = int(raw_input('Player#%s-->(Enter COLUMN you wanna mark) ' %(player))) - 1
    if col < 0 or col >= len(matrix[0]):
      print "Invalid COLUMN value!!!"
      continue
    if matrix[row][col] is not '#':
      print "Already played that position!!!, play again!!!"
      continue
    valid_input = 1
    num_plays += 1

  matrix[row][col] = player
  return row, col

def switch_player(player):
  if player is 'X':
     player = 'O'
  else:
    player = 'X'
  return player

def process_game(matrix, player, row, col):
   result = 1
   #import pdb; pdb.set_trace()
   for i in range(dims):
     if i is row:
       row_checks[player][i] += 1
       if row_checks[player][i] == dims:
         return 0, player
     if i is col:
       col_checks[player][i] += 1
       if col_checks[player][i] == dims:
         return 0, player

   if row is col:
     diag_checks[player] += 1
     if diag_checks[player] == dims:
       return 0, player
   if (row+col+1) is dims:
     r_diag_checks[player] += 1
     if r_diag_checks[player] == dims:
       return 0, player
   return result, ""

def start_game(matrix, player):
  global num_plays
  for i in range(len(matrix)):
    pprint(matrix[i])
  result = 1
  num_plays = 0
  while result:
    player = switch_player(player)
    row, col = get_input(matrix, player)
    result, winner = process_game(matrix, player, row, col)
    if result == 0:
      print "Winner is Player#%s" %(winner)
    if num_plays >= (dims*dims):
      print "Its a DRAW!!! "
      break
    for i in range(len(matrix)):
      pprint(matrix[i])
    #pprint(row_checks)
    #pprint(col_checks)
    #pprint(diag_checks)
    #pprint(r_diag_checks)

def main():
  global dims
  global row_checks
  global col_checks
  global diag_checks
  global r_diag_checks

  dims = int(raw_input('Enter num rows/columns:'))
  row_checks = {}
  row_checks['O'] = [ 0  for x in range(dims)]
  row_checks['X'] = [ 0  for x in range(dims)]
  col_checks = {}
  col_checks['O'] = [ 0  for x in range(dims)]
  col_checks['X'] = [ 0  for x in range(dims)]
  diag_checks = {}
  diag_checks['O'] = 0
  diag_checks['X'] = 0
  r_diag_checks = {}
  r_diag_checks['O'] = 0
  r_diag_checks['X'] = 0

  player = 'X'

  matrix = [['#' for x in range(dims)] for y in range(dims)]

  start_game(matrix, player)

if __name__ == '__main__':
  main()

