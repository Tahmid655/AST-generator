import ply.yacc as yacc
import ply.lex as lex

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

def create_tokeniser():
  # token names
  tokens = ("NUMBER","PLUS","MINUS","TIMES","DIVIDE","LPAREN","RPAREN")
  #regex expressions
  t_PLUS = r'\+' # the backslashes make sure that the regex meaning of "+" isn't used, it uses the raw "+" character.
  t_MINUS = r'-' #ply uses regex internally, therefore this must be done!
  t_TIMES = r'\*'
  t_DIVIDE = r'/'
  t_LBRACKET = r'\('
  t_RBRACKET = r'\)'

  def t_NUMBER(t):
    r'\d+' # useful regex to group strings of digits to make one number as the token.
    t.value = int(t.value) # converts into int
    return t

  t_ignore = ' \t' # skips spaces

  def t_error(t):
    raise ValueError(f"Illegal character '{t.value[0]}'")

  return lex.lex()
































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
'''
def tokenise(expression):
  tokens = []
  currentnumber=""

  for char in expression:
    if char.isdigit==True:
      currentnumber+=char # makes sure chains of multiple digits count as 1 number, e.g. "12"
    else:
      if currentnumber!="":
        tokens.append(currentnumber) # makes the current number a token as soon as the number finishes in the expression
        currentnumber=""

      elif char in "()+-*/=":
        tokens.append(char)
      elif char == " ":
        continue # skips spaces (obvious)
      else:
        print("ERROR unknown character ", char)
  if currentnumber!="":
    tokens.append(currentnumber)
    # adds the last number if there is any, required as the current system checks the next char and if that is not a digit,
    # then it adds the number as a token.

  return tokens

''' # mistake code, this is the tokeniser without using ply, i want to learn to use ply