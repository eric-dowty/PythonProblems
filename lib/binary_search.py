# Use binary search to find if a value is in a list

class BinarySearch:
  def __init__(self, list):
    self.list = list

  def find(self, val):
    found = self._find(val, 0, len(self.list) - 1)
    return found

  def _find(self, val, start_index, end_index):
    mid_index = (end_index + start_index) / 2

    if self.list[mid_index] == val:
      return True
    elif start_index >= len(self.list) - 1 or end_index <= 0:
      return False
    elif self.list[mid_index] > val:
      end_index = mid_index - 1
      return self._find(val, start_index, end_index)
    elif self.list[mid_index] < val:
      start_index = mid_index + 1
      return self._find(val, start_index, end_index)
