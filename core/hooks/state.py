from core.singletons.store import Store


class State:
    def _modifier(self, value):
        return self

    def __call__(self):
        return [self.value, self.modifier, self.uuid]

    def __init__(self, value) -> None:
        self.value = value
        # self.func =  func
        self.modifier = lambda _value: self._modifier(_value)
        self.uuid = str(self.modifier.__hash__())
        Store().addState(self)
