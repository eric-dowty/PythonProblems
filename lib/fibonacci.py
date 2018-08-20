# Create a class that compute a fibonacci series with n elements

class Fibonacci:
  def __init__(self, n):
    self.n = n
    self.current_sequence = []
    self._generate()

  @property
  def sequence(self):
    return self.current_sequence

  def _generate(self, n=0):
    n+=1
    if n > self.n:
      return
    elif n==1 or n==2:
      self.current_sequence.append(n)
      self._generate(n)
    else:
      next_val = sum(self.current_sequence[-2:])
      self.current_sequence.append(next_val)
      self._generate(n)
