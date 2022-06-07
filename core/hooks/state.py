from __future__ import annotations
from uuid import uuid4

from core.singletons.store import Store


class State:
    # def uuid(self) -> str:
    #     return str(id(self))
    #     # return self.__hash__()

    def _modifier(self, _value) -> State:
        self.value = _value
        return self

    # def __init__(self) -> None:
    # #     self.value = value
    # #     self.modifier = modifier
        # Store().addState(self)

    def __new__(self, value) -> None:
        self.value = value
        self.modifier = lambda _value: self._modifier(self, _value)
        self.uuid = self.modifier.__hash__()

        # self.modifier = modifier
        Store().addState(self)
        return [self.value, self.modifier, self.uuid]