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

if __name__ == '__main__':
    unittest.main()