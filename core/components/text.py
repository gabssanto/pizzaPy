from core.components.base_component import BaseComponent

class Text(BaseComponent):
    def __repr__(self) -> str:
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
          self.html += "<span class='value_" + str(self.value.__hash__()) + "'>" + str(self.value.value) + "</span>"

        string += '>' + self.html + '</span>' + self.script
        return string

    def __init__(self, className="", children={}, style={}, onClick="", script='', value=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
        self.value = value