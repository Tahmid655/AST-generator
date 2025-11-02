import ply.yacc as yacc
import ply.lex as lex

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
