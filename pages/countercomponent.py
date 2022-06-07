from core.components.button import Button
from core.components.div import Div
from core.components.text import Text

from core.hooks.state import State


def addCounter(counter: int):
    _value = counter + 1
    return _value


def rmvCounter(counter):
    return counter - 1


def CounterComponent(starting=1, increase=True):
    [value, setValue, uuid] = State(starting)
    [value2, setValue2, uuid2] = State(500)

    print(setValue.__hash__(), setValue2.__hash__(), 'carai')
    print(uuid, uuid2, 'carai')

    return Div(
        children=[
            Text(
                uuid=uuid,
                value=value
            ),
            "<br>",
            Button(
                uuid=uuid,
                onClick=setValue(addCounter(value)),
                children=["hit me"]
            ),
            "<br>",
            Text(
                uuid=uuid2,
                value=value2
            ),
            "<br>",
            Button(
                uuid=uuid2,
                onClick=setValue2(rmvCounter(value2)),
                children=["hit me2"]
            ),
        ]
    )
