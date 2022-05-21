from core.components.button import Button
from core.components.div import Div
from core.components.text import Text

from core.hooks.state import State


def addCounter(counter):
    return counter + 1


def rmvCounter(counter):
    return counter - 1


def CounterComponent(starting=1, increase=True):
    state = State(starting, addCounter if increase else rmvCounter)

    return Div(
        children=[
            Text(
                value=state
            ),
            "<br>",
            Button(
                onClick=state,
                children=["hit me"]
            ),
        ]
    )
