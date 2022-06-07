from core.singletons.store import Store


class State:
    def __init__(self, value, modifier) -> None:
        self.value = value
        # self.modifier =  modifier
        self.modifier = lambda _value: modifier(_value)
        Store().addState(self)
