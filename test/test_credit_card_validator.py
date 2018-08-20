import pytest
import sys
sys.path.append('../lib')

from credit_card_validator import CreditCardValidator

class TestCreditCardValidator:
  _valid_cc_number = '4123-4567-8912-3456'

  def setup_method(self, method):
    print ("setup_method      method:%s" % method.__name__)

  def teardown_method(self, method):
    print ("teardown_method   method:%s" % method.__name__)

  def test_it_returns_true_if_credit_card_starts_with_4(self):
    credit_card_validator = CreditCardValidator(self._valid_cc_number)
    assert credit_card_validator.validate() == True

  def test_it_returns_true_if_credit_card_starts_with_5(self):
    credit_card_validator = CreditCardValidator('5123456789123456')
    assert credit_card_validator.validate() == True

  def test_it_returns_true_if_credit_card_starts_with_6(self):
    credit_card_validator = CreditCardValidator('6123456789123456')
    assert credit_card_validator.validate() == True

  def test_it_returns_false_if_credit_card_does_not_start_with_4_5_or_6(self):
    credit_card_validator = CreditCardValidator('7123456789123456')
    assert credit_card_validator.validate() == False

  def test_it_returns_true_if_credit_card_has_exactly_16_digits(self):
    credit_card_validator = CreditCardValidator(self._valid_cc_number)
    assert credit_card_validator.validate() == True

  def test_it_returns_false_if_credit_card_has_more_than_16_digits(self):
    credit_card_validator = CreditCardValidator('5123-4567-8912-3456-7')
    assert credit_card_validator.validate() == False

  def test_it_returns_false_if_credit_card_has_less_than_16_digits(self):
    credit_card_validator = CreditCardValidator('5123-4567-8912-345')
    assert credit_card_validator.validate() == False

  def test_it_returns_true_if_credit_card_only_has_digits_and_dashes(self):
    credit_card_validator = CreditCardValidator(self._valid_cc_number)
    assert credit_card_validator.validate() == True

  def test_it_returns_false_if_credit_card_contains_chars_other_than_digits_and_dashes(self):
    credit_card_validator = CreditCardValidator('4123*4567*8912*3456')
    assert credit_card_validator.validate() == False

  def test_it_returns_false_if_dashes_are_used_and_digits_are_not_in_groups_of_four(self):
    credit_card_validator = CreditCardValidator('41234-567-8912-3456')
    assert credit_card_validator.validate() == False