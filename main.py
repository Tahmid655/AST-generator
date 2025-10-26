class ASTNode:
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def __repr__(self):
    return str(self.value)

  def print_tree(self,level=0):
    print(" " * (4*level) + str(self.value))
    for child in self.children:
      child.print_tree(level+1)
'''
# TEST ASTNODE CLASS BY USING 2 + 3 * (4 - 1)
n1 = ASTNode(2, [])
n2 = ASTNode(3, [])
n3 = ASTNode(4, [])
n4 = ASTNode(1, [])
sub = ASTNode('-', [n3, n4])
mul = ASTNode('*', [n2, sub])
root = ASTNode('+', [n1, mul])

root.print_tree()
'''