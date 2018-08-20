import pytest
import sys
sys.path.append('../lib')

from first import First

class TestFirst:
  def setup_method(self, method):
    print ("setup_method      method:%s" % method.__name__)

  def teardown_method(self, method):
    print ("teardown_method   method:%s" % method.__name__)

  def test_get_val(self):
    first = First(5)

    assert first.get_val() == 5