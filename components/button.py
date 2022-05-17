from components.base_component import BaseComponent

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
            string += ' onclick="changeData(' + str(self.onClick.__hash__()) + ')"'

        string += '>' + self.html + '</button>' + self.script
        return string

    def __init__(self, className="", children={}, style={}, onClick="", script=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''