from renderer import Renderer

class BaseHTMLComponent:
  def __init__(self, type, id=None, className=None, children=[]):
    self._id = id
    self._className = className
    self._children = children
    self._type = type
    self._loadElement()
    
  def _loadElement(self):
    self._element = {
      "type": self._type,
      "props": {}
    }

    if self._id:
      self._element["props"]["id"] = self._id

    if self._className:
      self._element["props"]["className"] = self._className

    if len(self._children) > 0:
      self._element["props"]["children"] = [child.element for child in self._children]

  @property
  def element(self):
    return self._element

class Text(BaseHTMLComponent):
  def __init__(self, value=""):
    super().__init__(type="text")
    self._element["props"]["value"] = value

class Div(BaseHTMLComponent):
  def __init__(self, id=None, className=None, children=[]):
    super().__init__("div", id, className, children)

class Span(BaseHTMLComponent):
  def __init__(self, id=None, className=None, children=[]):
    super().__init__("span", id, className, children)

class Link(BaseHTMLComponent):
  def __init__(self, id=None, className=None, href=None, children=[]):
    super().__init__("a", id, className, children)

    if href:
      self._element["props"]["href"] = href

class Button(BaseHTMLComponent):
  def __init__(self, id=None, className=None, onClick=None, children=[]):
    super().__init__("button", id, className, children)

    if onClick:
      self._element["props"]["onClick"] = onClick

class Input(BaseHTMLComponent):
  def __init__(self, id=None, className=None, type=None, value=None):
    super().__init__("input", id, className, [])

    if type:
      self._element["props"]["type"] = type
    
    if value:
      self._element["props"]["value"] = value

class StatefulComponent:
  def __init__(self, props) -> None:
    self.props = props
    self.state = {}
    self.__internalInstance = None

  def setState(self, newState):
    self.state = newState
    Renderer.updateInstance(self.__internalInstance)

  def setInternalInstance(self, internalInstance):
    self.__internalInstance = internalInstance

  @property
  def element(self):
    el = {
      "type": self.__class__,
      "props": {}
    }
    for prop in self.props:
      el["props"][prop] = self.props[prop]
    return el

  def render(self):
    pass