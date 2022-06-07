from core.singletons.store import Store


class State:
    def __init__(self, value, modifier) -> None:
        self.value = value
        self.modifier = modifier
        Store().addState(self)
