from components import StatefulComponent, Div, Span, Button, Text
from renderer import Renderer
from pyscript import Element

class SubComponent(StatefulComponent):
  def __init__(self, title) -> None:
    super().__init__({ "title": title })
    self.state = {
      "counter": 0
    }

  def add(self, *args):
    counter = self.state["counter"] + 1
    self.setState({
      "counter": counter
    })

  def render(self):
    return Div(
      children=[
        Span(
          children=[Text(self.props["title"]), Text(self.state["counter"])]
        ),
        Button(
          onClick=self.add,
          children=[Text("Add")]
        )
      ]
    )

class MainPage(StatefulComponent):
  def __init__(self) -> None:
    super().__init__({})

  def render(self):
    return Div(
      children=[SubComponent("Component 1: "), SubComponent("Component 2: ")]
    )

Renderer.render(MainPage().element, Element("root"))