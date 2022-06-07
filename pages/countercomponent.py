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
    [value, setValue] = State(starting)
    [value2, setValue2] = State(500)

    print(setValue.__hash__(), setValue2.__hash__(), 'carai')

    return Div(
        children=[
            Text(
                value=value
            ),
            "<br>",
            Button(
                uuid=setValue.__hash__(),
                onClick=setValue(addCounter(value)),
                children=["hit me"]
            ),
            "<br>",
            Text(
                value=value2
            ),
            "<br>",
            Button(
                uuid=setValue2.__hash__(),
                onClick=setValue2(rmvCounter(value2)),
                children=["hit me2"]
            ),
        ]
    )
