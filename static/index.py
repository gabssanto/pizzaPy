from components import *

def heyyea(self):
  print("HEEEEEEEEEYYYYYYYYYYYEEEAAAAAAAA")

def MainPage():
  return Div(
    id="container",
    children=[
      Div(
        children=[
          Input(
            type="text",
            value="Inputzin"
          ),
          Link(
            className="color-primary",
            href="http://google.com",
            children=[
              Text("Linkzin")
            ]
          )
        ]
      ),
      Div(
        children=[
          Span(
            children=[
              Text("Hello there")
            ]
          ),
          Button(
            onClick=heyyea,
            children=[
              Text("Hit me")
            ]
          )
        ]
      )
    ]
  )

Renderer.render(MainPage().element, Element("root"))