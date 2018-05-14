#
# Tree Library
#

class Node():
  def __init__(self, val, left=None, right=None):
    self.left = left
    self.right = right
    self.val = val

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  def get_value(self):
    return self.val

class Tree():
  def __init__(self, sorted_arr=None):
    self.root = None
    if sorted_arr:
      self.root = self._build_binary_search_tree(sorted_arr, 0, len(sorted_arr)-1)

  def _build_binary_search_tree(self, arr, start, end):
    if start > end:
      return None
    mid = (start+end)/2
    node = Node(arr[mid])
    node.left = self._build_binary_search_tree(arr, start, mid-1)
    node.right =self._build_binary_search_tree(arr, mid+1, end)
    return node

  def _print_inorder(self, node):
    if node.left:
      self._print_inorder(node.left)
    print "==> %d" %(node.val)
    if node.right:
      self._print_inorder(node.right)

  def _print_inorder(self, node):
    print "==> %d" %(node.val)
    if node.left:
      self._print_inorder(node.left)
    if node.right:
      self._print_inorder(node.right)

  def _print_postorder(self, node):
    if node.left:
      self._print_inorder(node.left)
    if node.right:
      self._print_inorder(node.right)
    print "==> %d" %(node.val)

  def get_root(self):
    return self.root

  def print_inorder(self):
    self._print_inorder(self.root)

  def print_preorder(self):
    self._print_preorder(self.root)

  def print_postorder(self):
    self._print_postorder(self.root)

