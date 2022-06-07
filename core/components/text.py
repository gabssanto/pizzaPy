from core.components.base_component import BaseComponent

class Text(BaseComponent):
    def __repr__(self) -> str:
        return self.mount_updatable_component()

    def __init__(self, className="", children={}, style={}, onClick="", script='', value=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
        self.value = value