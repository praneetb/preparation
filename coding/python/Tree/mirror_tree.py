#
# mirror a binary tree
#
import tree
from Queue import Queue


def mirror(node):
  if not node:
    return 
  mirror(node.left)
  mirror(node.right)
  tmp = node.left
  node.left = node.right
  node.right = tmp

def mirror_iter(node):
  q = Queue()
  q.put(node)
  while not q.empty():
    n = q.get()
    tmp = n.left
    n.left = n.right
    n.right = tmp
    if n.left:
      q.put(n.left)
    if n.right:
      q.put(n.right)

def main():
  sorted_array = [0, 12, 2, 3, 5, 7 ]
  print sorted_array
  t = tree.Tree(sorted_array)
  t.print_inorder()
  mirror_iter(t.root)
  print "Mirror:"
  t.print_inorder()

if __name__ == '__main__':
  main()


