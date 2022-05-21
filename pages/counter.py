from core.components.div import Div
from core.router import Router


def counterPage(route=None):
    return Div(
        className="container",
        children=[
            Router().render("counter", route)
        ]
    )
