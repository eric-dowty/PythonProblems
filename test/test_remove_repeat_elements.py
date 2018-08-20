import pytest
import sys
sys.path.append('../lib')

from remove_repeat_elements import remove_repeat_elements

class TestRemoveRepeatElements:
  def setup_method(self, method):
    print ("setup_method      method:%s" % method.__name__)

  def teardown_method(self, method):
    print ("teardown_method   method:%s" % method.__name__)

  def test_it_removes_duplicate_elements(self):
    assert remove_repeat_elements([1,2,2,2,3,3,4,5]) == [1,2,3,4,5]

  def test_it_returns_a_list_object(self):
    return_val = remove_repeat_elements([1])
    assert type(return_val) is list