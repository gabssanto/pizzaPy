from core.components.button import Button
from core.components.div import Div
from core.router import Router


def HomeComponent():

    return Div(
        children=[
            Button(
                onClick=Router().navigate("counter", "/pag1"),
                children=["Pag1"]
            ),
            Button(
                onClick=Router().navigate("counter", "/pag2"),
                children=["Pag2"]
            )
        ]
    )
