from core.components.base_component import BaseComponent
from core.router import RouterNavigate
from core.hooks.state import State


class Button(BaseComponent):
    def __repr__(self) -> str:
        for child in self.children:
            self.html = self.html + str(child)

        string = '<button'

        if self.className != '':
            string += ' class="' + self.className + '"'

        if self.style != '':
            string += ' style="' + self.style + '"'

        if self.onClick != '':
            if type(self.onClick) is State:
                string += ' onclick="changeData(' + \
                    str(self.onClick.__hash__()) + ')"'
            elif type(self.onClick) is RouterNavigate:
                string += ' onclick="' + self.onClick.value() + '"'
            else:
                string += ' onclick="' + self.onClick + '"'

        string += '>' + self.html + '</button>' + self.script
        return string

    def __init__(self, className="", children={}, style={}, onClick="", script=''):
        super().__init__()
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
