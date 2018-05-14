# check if tree is BST
import tree
import sys

max_int = sys.maxint
min_int = -max_int-1

def check_bst(node, min, max):
  if not node:
    return True
  if node.get_value() < min or node.get_value() > max:
    return False
  if not check_bst(node.left, min, node.get_value()):
    return False
  if not check_bst(node.right, node.get_value(), max):
    return False
  return True

def main():
  sorted_array = [0, 12, 2, 3, 5, 7 ]
  t = tree.Tree(sorted_array)
  if t.root:
    print check_bst(t.root, min_int, max_int)
  else:
    print "Null Tree"

if __name__ == '__main__':
  main()

