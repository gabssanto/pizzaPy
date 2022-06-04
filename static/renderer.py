from js import document
from pyodide import create_proxy

class Renderer:
  @staticmethod
  def render(element, parent):
    type = element["type"]
    props = element["props"]

    if type == "text":
      parent.write(props["value"])
      return

    id = None
    if "id" in props:
      id = props["id"]

    className = ""
    if "className" in props:
      className = props["className"]

    elementDom = create(type, id, className)

    for key in props:
      if key[:2] == "on":
        eventType = key[2:].lower()
        elementDom.element.addEventListener(eventType, create_proxy(props[key]))

    for key in props:
      if key[:2] != "on" and key != "children" and key != "id" and key != "className":
        elementDom.add_prop(key, props[key])

    children = props["children"] if "children" in props else []
    parent.element.appendChild(elementDom.element)

    for childElement in children:
      Renderer.render(childElement, elementDom)