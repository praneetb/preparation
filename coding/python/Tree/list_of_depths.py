# list of depths at each level
import tree

def traverse_levels(lls, node, level):
  # traverse pre-order
  if not node:
    return
  if level in lls:
    lls[level].append(node.get_value())
  else:
    lls[level] = [node.get_value()]
  traverse_levels(lls, node.get_left(), level+1)
  traverse_levels(lls, node.get_right(), level+1)

def main():
  sorted_array = [0, 2, 3, 5, 7 ]
  t = tree.Tree(sorted_array)
  lls = {}
  traverse_levels(lls, t.get_root(), 0)
  print lls

if __name__ == '__main__':
  main()
