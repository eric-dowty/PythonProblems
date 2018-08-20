import re

class CreditCardValidator:
  def __init__(self, cc_number):
    self.cc_number = cc_number

  def validate(self):
    return all([
      self._starts_with_4_5_or_6(),
      self._contains_exactly_16_digits(),
      self._contains_only_digits_and_dashes(),
      self._digits_in_groups_of_four()
    ])

  def _starts_with_4_5_or_6(self):
    regex = r'\A[456]'
    return re.match(regex, self.cc_number)

  def _contains_exactly_16_digits(self):
    cc_digits = re.sub('\D', '', self.cc_number)
    return len(cc_digits) == 16

  def _contains_only_digits_and_dashes(self):
    valid_chars = '0123456789-'
    return all(char in valid_chars for char in self.cc_number)

  def _digits_in_groups_of_four(self):
    if '-' not in self.cc_number:
      return True
    else:
      digit_groups = self.cc_number.split('-')
      return all(len(group) == 4 for group in digit_groups)