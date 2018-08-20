import pytest
import sys
sys.path.append('../lib')

from reverse_word_order import ReverseWordOrder

class TestReverseWordOrder:
  def setup_method(self, method):
    print ("setup_method      method:%s" % method.__name__)

  def teardown_method(self, method):
    print ("teardown_method   method:%s" % method.__name__)

  def test_it_reverses_the_word_order_of_a_string(self):
    string_reverser = ReverseWordOrder("This is a string to be reversed.")
    assert string_reverser.reverse() == "reversed. be to string a is This"