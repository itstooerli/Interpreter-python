from enum import Enum

## Define Constants
OPERATORS = {'+' : 1, '-' : 1, '*' : 2, '/' : 2} # Defines symbol : order of precedence, greater number higher precedence

class Term(Enum):
  NONE = 0
  OPERAND = 1
  OPERATOR = 2

def tokenize(expr: str) -> list:
  """Takes an expression and returns an array with each term as the correct type

  Parameters
  expr : string
    The expression to tokenize

  Returns
    An array with each term as the correct type, empty array if invalid token
  """
  parsed_expr = []
  if isinstance(expr, str):
    curr_num = ""
    for char in expr:
      if char.isnumeric():
        curr_num += char
      elif char in OPERATORS:
        if curr_num:
          parsed_expr.append(int(curr_num))
          curr_num = ""
        parsed_expr.append(char)
      elif char.isspace():
        if curr_num:
          parsed_expr.append(int(curr_num))
          curr_num = ""
      else:
        print(f'Token Error - Invalid Character {char}')
        return []

    if curr_num:
      parsed_expr.append(int(curr_num))
      
  return parsed_expr

def parse(expr: list) -> list:
  """Takes a list that represents an expression and returns an array with the terms in postfix format

  Parameters
  expr : string
    list of terms representing the expression

  Returns
    An array in postfix format or an empty array if expression invalid
  """
  postfix_expr = []
  stack = []
  prevType = Term.NONE
  for term in expr:
    if isinstance(term, int) or isinstance(term, float):
      if prevType == Term.OPERAND:
        print('Parse Error - Cannot have two consecutive operands')
        return []
      postfix_expr.append(term)
      prevType = Term.OPERAND
    elif term in OPERATORS:
      while stack and OPERATORS[term] <= OPERATORS[stack[-1]]:
         postfix_expr.append(stack.pop())
      stack.append(term)
      prevType = Term.OPERATOR
    else:
      print(f'Parse Error - {term} not recognized.')
      return []

  while stack:
    postfix_expr.append(stack.pop())
  
  return postfix_expr

def interpret(expr: list) -> int | float | None:
  """Takes a list that represents an expression and returns the result of the expression

  Parameters
  expr : string
    list of terms representing the expression in postfix format

  Returns
    The result of the simplified expression
  """
  stack = []

  for term in expr:
    if term == '+':
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append(operand2 + operand1)
    elif term == '-':
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append(operand2 - operand1)
    elif term == '*':
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append(operand2 * operand1)
    elif term == '/':
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append(operand2 / operand1)
    else:
      stack.append(term)

  if len(stack) != 1:
    print('Interpeter Error - Invalid expression')
    return None
    
  return stack.pop()

def main():
  done = False
  while not done:
    user_input = input('Expression: ')
    if user_input == "":
      break

    token_expr = tokenize(user_input)
    
    if not token_expr:
      break

    parsed_expr = parse(token_expr)

    if not parsed_expr:
      break

    interpreted_expr = interpret(parsed_expr)

    if interpreted_expr == None:
      break
      
    print(interpreted_expr)

if __name__ == "__main__":
  main()

