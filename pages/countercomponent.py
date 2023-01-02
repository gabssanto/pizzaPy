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
    [value, setValue, uuid] = State(starting)()
    print(value, setValue, 'coroi')

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
        ]
    )
