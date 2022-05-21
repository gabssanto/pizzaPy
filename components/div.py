from components.base_component import BaseComponent


class Div(BaseComponent):
    def __repr__(self) -> str:
        for child in self.children:
            self.html = self.html + str(child)

        string = '<div'

        if self.className != '':
            string += ' class="' + self.className + '"'

        if self.style != '':
            string += ' style="' + self.style + '"'

        if self.onClick != '':
            string += ' onclick="() => ' + str(self.onClick) + '"'

        if self.onLoad != '':
            string += ' onload="' + self.onLoad + '"'

        string += '>' + self.html + '</div>' + self.script
        return string

    def __init__(self, className="", children={}, style={}, onClick="", script='', onLoad=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
        self.onLoad = onLoad