
from core.components.div import Div
from core.components.input import Input

def indexPage():
    return Div(className="container", children=[
            'hello', Div(children=['world', Input(className="input")])])
