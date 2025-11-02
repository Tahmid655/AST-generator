from ast_node import *
from lexer import *

precedence = (
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE'),
)

#p[0] is the final result of the operation
#p[1] is the left bit of the expression, usually a number
#p[2] is the operation
#p[3] is the right bit of the operation, usually a number.

def one_operation(p): # deals with calculations with only one operation (e.g. 1+1)
  p[0]=ASTNode(p[2],[p[1],p[3]])

def parenthesis(p):
  p[0]=p[2] # parenthesis changes order, the parenthesis is always done first by law of BIDMAS.

def number(p):
  p[0]=ASTNode(p[1],[])

def error(p):
  print("Syntax Error")

parser = yacc.yacc()