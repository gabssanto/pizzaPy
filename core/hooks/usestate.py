from core.singletons.store import Store

# Auto update the state when the value is changed
class UseState:
  stack = []
  current_value = None

  def get_state(self):
    return self.current_value

  def set_state(self, value):
    self.current_value = value
    self.stack.append(value)

  def __init__(self, value) -> None:
      self.value = value
      self.stack.append(value)
      self.current_value = self.value

  def __repr__(self) -> str:
      return str(self.current_value)

  def __call__(self, *args, **kwargs):
      # self.current_value = self.value
      # self.value = self.modifier(self.value)
    return self.__repr__, self.set_state

