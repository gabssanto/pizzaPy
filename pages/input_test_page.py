from core.components.div import Div
from core.components.input import Input
from core.hooks.state import State

def onchange(state, value):
    return state + value

def input_test_page():
    state = State("", onchange)
    return Div(className="container", children=[
            'hello', Div(children=['world', Input(className="input", onChange=state)])])