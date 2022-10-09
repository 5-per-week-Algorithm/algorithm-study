class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:

  if p == q:
    return True

  if p.val != q.val:
    return False
  else:
    result = True

  if p.left or q.left is not None :
    if p.left and q.left is not None:
      result = isSameTree(p.left, q.left)
    else:
      return False
  if p.right or q.right is not None:
    if p.right and q.right is not None:
      result = isSameTree(p.right, q.right)
    else:
      return False


  return result

# p = TreeNode(1, TreeNode(5), TreeNode(-2))
# q = TreeNode(1, TreeNode(5), TreeNode(-2))
#
# The answer is True.
# print(isSameTree(p,q))
#
# p = TreeNode(0, TreeNode(2))
# q = TreeNode(0, None, TreeNode(2))
#
# # The answer is False.
# print(isSameTree(p,q))

# p = TreeNode(3, TreeNode(7, TreeNode(2), None), TreeNode(15, TreeNode(6), TreeNode(-1)))
# q = TreeNode(3, TreeNode(7, TreeNode(2), None), TreeNode(15, TreeNode(-1), TreeNode(6)))
#
# The answer is False.
# print(isSameTree(p,q))
#
# p = None
# q = None
#
# # The answer is True.
# print(isSameTree(p,q))