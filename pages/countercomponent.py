from components.button import Button
from components.div import Div
from components.text import Text

from core.state import State


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
