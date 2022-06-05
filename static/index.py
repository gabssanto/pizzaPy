from components import *

class MainPage:
  counter = 0

  def add(self, *args):
    self.counter += 1
    Renderer.render(self.render().element, Element("root"))

  def render(self):
    return Div(
      id="container",
      children=[
        Span(
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