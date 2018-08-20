import pytest
import sys
sys.path.append('../lib')

from binary_search import BinarySearch

class TestBinarySearch:
  _ordered_list = [1,2,3,4,5,7,9,15,17,20,27]

  def setup_method(self, method):
    print ("setup_method      method:%s" % method.__name__)

  def teardown_method(self, method):
    print ("teardown_method   method:%s" % method.__name__)

  def test_it_should_return_true_if_root_node_is_val(self):
    binary_search = BinarySearch(self._ordered_list)
    assert binary_search.find(7) == True

  def test_it_should_search_the_left_side(self):
    binary_search = BinarySearch(self._ordered_list)
    assert binary_search.find(3) == True

  def test_it_should_search_the_right_side(self):
    binary_search = BinarySearch(self._ordered_list)
    assert binary_search.find(17) == True

  def test_it_should_return_false_if_val_not_in_list_high_val(self):
    binary_search = BinarySearch(self._ordered_list)
    assert binary_search.find(21) == False

  def test_it_should_return_false_if_val_not_in_list_low_val(self):
    binary_search = BinarySearch(self._ordered_list)
    assert binary_search.find(0) == False
