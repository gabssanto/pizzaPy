
from components.div import Div

def indexPage():
    return Div(className="container", children=[
            'hello', Div(children=['world'])])