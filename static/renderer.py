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
    elif instance["element"]["type"] == element["type"]:
      if element["type"] != "text":
        Renderer.updateProps(instance["dom"], instance["element"]["props"], element["props"])
        instance["childInstances"] = Renderer.reconcileChildren(instance, element)
        instance["element"] = element
        return instance
      else:
        if instance["element"]["props"]["value"] != element["props"]["value"]:
          newInst = Renderer.getInstance(element)
          parentDom.element.replaceChild(newInst["dom"].element, instance["dom"].element)
          return newInst
        else:
          return instance
    else:
      newInst = Renderer.getInstance(element)
      parentDom.element.replaceChild(newInst["dom"].element, instance["dom"].element)
      return newInst

  @staticmethod
  def reconcileChildren(instance, element):
    elementDom = instance["dom"]
    childInstances = instance["childInstances"]
    
    nextChildElements = element["props"]["children"] if "children" in element["props"] else []
    nextChildInstances = []

    size = max(len(nextChildElements), len(childInstances))
    for i in range(size):
      newChildInstance = Renderer.reconcile(elementDom, childInstances[i], nextChildElements[i])
      nextChildInstances.append(newChildInstance)

    return nextChildInstances

  @staticmethod
  def updateProps(elementDom, prevProps, nextProps):
    for key in prevProps:
      if key[:2] == "on":
        eventType = key[2:].lower()
        elementDom.element.removeEventListener(eventType, elementDom._function)
        elementDom._function.destroy()

    for key in prevProps:
      if key[:2] != "on" and key != "children" and key != "id" and key != "className":
        elementDom.element.removeAttribute(key)
      elif key == "className" and prevProps[key] != "":
        elementDom.element.removeAttribute("class")

    for key in nextProps:
      if key[:2] == "on":
        eventType = key[2:].lower()
        elementDom._function = create_proxy(nextProps[key])
        elementDom.element.addEventListener(eventType, elementDom._function)

    for key in nextProps:
      if key[:2] != "on" and key != "children" and key != "id" and key != "className":
        elementDom.element.setAttribute(key, nextProps[key])
      elif key == "className" and nextProps[key] != "":
        add_classes(elementDom.element, nextProps[key])


  @staticmethod
  def getInstance(element):
    type = element["type"]
    props = element["props"]

    if type == "text":
      elementNode = document.createTextNode(props["value"])
      elementDom = Element(None, elementNode)
      return {
        "dom": elementDom,
        "element": element,
        "childInstances": []
      }

    id = None
    if "id" in props:
      id = props["id"]

    elementDom = create(type, id)

    Renderer.updateProps(elementDom, [], props)

    childElements: list = props["children"] if "children" in props else []

    childInstances = []
    for childElement in childElements:
      childInstance = Renderer.getInstance(childElement)
      childInstances.append(childInstance)
      elementDom.element.appendChild(childInstance["dom"].element)

    return {
      "dom": elementDom,
      "element": element,
      "childInstances": childInstances
    }
