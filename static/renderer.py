from js import document
from pyodide import create_proxy 

class Renderer:
  rootInstance = None

  @staticmethod
  def render(element, parentDom):
    prevInst = Renderer.rootInstance
    nextInst = Renderer.reconcile(parentDom, prevInst, element)
    Renderer.rootInstance = nextInst

  @staticmethod
  def reconcile(parentDom, instance, element):
    if instance == None:
      newInst = Renderer.getInstance(element)
      parentDom.element.appendChild(newInst["dom"].element)
      return newInst
    else:
      newInst = Renderer.getInstance(element)
      parentDom.element.replaceChild(newInst["dom"].element, instance["dom"].element)
      return newInst

  @staticmethod
  def getInstance(element):
    type = element["type"]
    props = element["props"]

    if type == "text":
      return {
        "dom": None,
        "element": element,
        "instances": None
      }

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

    children: list = props["children"] if "children" in props else []

    childInstances = []
    for childElement in children:
      childInstance = Renderer.getInstance(childElement)
      childInstances.append(childInstance)

      if childInstance["dom"]:
        elementDom.element.appendChild(childInstance["dom"].element)
      else:
        elementDom.write(childInstance["element"]["props"]["value"])

    return {
      "dom": elementDom,
      "element": element,
      "instances": childInstances
    }
