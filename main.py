from enum import Enum

class Operator(Enum):
  ADD = '+'
  SUBTRACT = '-'
  MULTIPLY = '*'
  DIVIDE = '/'
  
  @classmethod
  def has_value(cls, value):
    return value in [item.value for item in Operator]

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
      elif Operator.has_value(char):
        if curr_num:
          parsed_expr.append(int(curr_num))
          curr_num = ""
        parsed_expr.append(char)
      elif char.isspace():
        if curr_num:
          parsed_expr.append(int(curr_num))
          curr_num = ""
      else:
        print(f'Invalid Character {char}')
        return []

    if curr_num:
      parsed_expr.append(int(curr_num))
      
  return parsed_expr

def main():
  done = False
  while not done:
    user_input = input('Expression: ')
    if user_input == "":
      break

    parsed_expr = tokenize(user_input)
    
    if not parsed_expr:
      break

    print(parsed_expr)

if __name__ == "__main__":
  main()

