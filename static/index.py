from components import *

class MainPage:
  counter = 0
  classNameVar = "blue"

  def add(self, *args):
    self.counter += 1
    self.classNameVar = "blue" if self.classNameVar == "red" else "red"
    Renderer.render(self.render().element, Element("root"))

  def render(self):
    return Div(
      id="container",
      children=[
        Span(
          className=self.classNameVar,
          children=[
            Text("ue")
          ]
        ),
        Div(
          children=[
            Span(
              children=[
                Text(self.counter)
              ]
            ),
            Button(
              onClick=self.add,
              children=[
                Text("Hit me")
              ]
            )
          ]
        )
      ]
    )

Renderer.render(MainPage().render().element, Element("root"))