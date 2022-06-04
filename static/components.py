class BaseComponent:
  def __init__(self, id=None, className=None, children=[]):
    self._id = id
    self._className = className
    self._children = children
    self._type = ""
    
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

class Text(BaseComponent):
  def __init__(self, value=""):
    super().__init__()
    self._type = "text"
    self._loadElement()
    self._element["props"]["value"] = value

class Div(BaseComponent):
  def __init__(self, id=None, className=None, children=[]):
    super().__init__(id, className, children)
    self._type = "div"
    self._loadElement()

class Span(BaseComponent):
  def __init__(self, id=None, className=None, children=[]):
    super().__init__(id, className, children)
    self._type = "span"
    self._loadElement()

class Link(BaseComponent):
  def __init__(self, id=None, className=None, href=None, children=[]):
    super().__init__(id, className, children)
    self._type = "a"
    self._loadElement()

    if href:
      self._element["props"]["href"] = href

class Button(BaseComponent):
  def __init__(self, id=None, className=None, onClick=None, children=[]):
    super().__init__(id, className, children)
    self._type = "button"
    self._loadElement()

    if onClick:
      self._element["props"]["onClick"] = onClick

class Input(BaseComponent):
  def __init__(self, id=None, className=None, type=None, value=None):
    super().__init__(id, className, [])
    self._type = "input"
    self._loadElement()

    if type:
      self._element["props"]["type"] = type
    
    if value:
      self._element["props"]["value"] = value