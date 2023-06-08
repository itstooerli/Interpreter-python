import unittest
from main import *

class TestTokenize(unittest.TestCase):
  def test_tokenize_invalid_type(self):
    """
    Test tokenization of invalid type
    """
    data = 1
    result = tokenize(data)
    self.assertEqual(result, [])
  
  def test_tokenize_basic_add(self):
    """
    Test tokenization of numbers and '+'
    """
    data = '2 + 1'
    result = tokenize(data)
    self.assertEqual(result, [2,'+',1])
    
  def test_tokenize_basic_subtract(self):
    """
    Test tokenization of numbers and '-'
    """
    data = '2 - 1'
    result = tokenize(data)
    self.assertEqual(result, [2,'-',1])

  def test_tokenize_basic_multiply(self):
    """
    Test tokenization of numbers and '*'
    """
    data = '2 * 1'
    result = tokenize(data)
    self.assertEqual(result, [2,'*',1])

  def test_tokenize_basic_divide(self):
    """
    Test tokenization of numbers and '/'
    """
    data = '2 / 1'
    result = tokenize(data)
    self.assertEqual(result, [2,'/',1])

  def test_tokenize_basic_numbers(self):
    """
    Test tokenization of numbers and spaces
    """
    data = '111 11 1 1'
    result = tokenize(data)
    self.assertEqual(result, [111,11,1,1])

  def test_tokenize_invalid_characters(self):
    """
    Test tokenization of invalid characters
    """
    data = '1 & 1'
    result = tokenize(data)
    self.assertEqual(result, [])

  def test_tokenize_multiple_operators(self):
    """
    Test tokenization of numbers and '/'
    """
    data = '2 + 1 / 3 * 4 - 5'
    result = tokenize(data)
    self.assertEqual(result, [2,'+',1,'/',3,'*',4,'-',5])

class TestParse(unittest.TestCase):
  def test_parse_basic_add(self):
    """
    Test parsing of add expression
    """
    data = tokenize('2 + 1')
    result = parse(data)
    self.assertEqual(result, [2,1,'+'])

  def test_parse_basic_subtract(self):
    """
    Test parsing of subtract expression
    """
    data = tokenize('2 - 1')
    result = parse(data)
    self.assertEqual(result, [2,1,'-'])

  def test_parse_basic_multiply(self):
    """
    Test parsing of add expression
    """
    data = tokenize('2 * 1')
    result = parse(data)
    self.assertEqual(result, [2,1,'*'])

  def test_parse_basic_divide(self):
    """
    Test parsing of add expression
    """
    data = tokenize('2 / 1')
    result = parse(data)
    self.assertEqual(result, [2,1,'/'])

  def test_parse_basic_invalid_consecutive_numbers(self):
    """
    Test parsing of add expression
    """
    data = tokenize('2 2 + 1')
    result = parse(data)
    self.assertEqual(result, [])

  def test_parse_multiple_operators(self):
    """
    Test parsing of add expression
    """
    data = tokenize('1 + 2 * 3 + 4')
    result = parse(data)
    self.assertEqual(result, [1,2,3,'*','+',4,'+'])

if __name__ == '__main__':
    unittest.main()