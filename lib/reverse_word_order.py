class ReverseWordOrder:
  def __init__(self, input_string):
    self.input_string = input_string

  def reverse(self):
    words = self.input_string.split()
    words.reverse()
    return (' ').join(words)
