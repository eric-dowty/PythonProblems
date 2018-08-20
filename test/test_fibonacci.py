import pytest
import sys
sys.path.append('../lib')

from fibonacci import Fibonacci

class TestFibonacci:
  def setup_method(self, method):
    print ("setup_method      method:%s" % method.__name__)

  def teardown_method(self, method):
    print ("teardown_method   method:%s" % method.__name__)

  def test_it_returns_correct_sequence_if_input_is_1(self):
    fibonacci = Fibonacci(1)
    assert fibonacci.sequence == [1]

  def test_it_returns_correct_sequence_if_input_is_2(self):
    fibonacci = Fibonacci(2)
    assert fibonacci.sequence == [1,2]

  def test_it_returns_correct_sequence_if_input_is_3(self):
    fibonacci = Fibonacci(3)
    assert fibonacci.sequence == [1,2,3]

  def test_it_returns_correct_sequence_if_input_is_more_than_3(self):
    fibonacci = Fibonacci(9)
    assert fibonacci.sequence == [1, 2, 3, 5, 8, 13, 21, 34, 55]