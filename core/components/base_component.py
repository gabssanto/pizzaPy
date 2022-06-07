from core.hooks.state import State
from core.router import RouterNavigate


class BaseComponent:
    """
    Base class for all components.
    """
    def __init__(self, className="", children={}, style={}, onClick="", script='', onLoad=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
        self.onLoad = onLoad
    
    def attribute_exists(self, type: str) -> bool:
        return hasattr(self, type) and getattr(self, type) != ''

    def mount_updatable_component(self) -> str:
        for child in self.children:
            self.html = self.html + str(child)

        string = '<span'

        if self.className != '':
            string += ' class="' + self.className + ' updatable"'
        else:
            string += ' class="updatable"'

        if self.style != '':
            string += ' style="' + self.style + '"'

        if self.onClick != '':
            string += ' onclick="' + str(self.onClick) + '"'

        if self.value != '':
          self.html += "<span class='value_" + str(self.value.__hash__()) + "'>" + str(self.value) + "</span>"

        string += '>' + self.html + '</span>' + self.script
        return string

    def mount_children_component(self, tag: str) -> str:
        for child in self.children:
            self.html = self.html + str(child)

        string = f'<{tag}'

        if self.attribute_exists("className"):
            string += ' class="' + self.className + '"'

        if self.attribute_exists("style"):
            string += ' style="' + self.style + '"'

        if self.attribute_exists("onClick"):
            if self.onClick.__name__ is 'State':
                string += ' onclick="changeData(' + \
                    str(self.uuid) + ')"'
            elif self.onClick.__name__ is 'RouterNavigate':
                string += ' onclick="' + self.onClick.value() + '"'
            else:
                string += ' onclick="' + self.onClick + '"'

        if self.attribute_exists("onLoad"):
            string += ' onload="' + self.onLoad + '"'

        if self.attribute_exists("value"):
          self.html += "<span class='value_" + str(self.value.__hash__()) + "'>" + str(self.value.value) + "</span>"

        string += '>' + self.html + f'</{tag}>' + self.script
        return string

    def mount_self_closing_component(self, tag: str) -> str:
        string = f'<{tag}'

        if self.src: 
            string += f' src="{self.src}"'

        string += '/>'
        return string

    def parseKey(self, key: str) -> str:
        if key == 'backgroundColor':
            return 'background-color'
        return ''

    def mountStyle(self, style: dict) -> str:
        string = ''
        for key in style:
            string += self.parseKey(key) + ':' + style[key] + ';'
        return string
