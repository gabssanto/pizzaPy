from core.components.base_component import BaseComponent


class Div(BaseComponent):
    def __repr__(self) -> str:
        return self.mount_children_component('div')
        
    def __init__(self, className="", children={}, style={}, onClick="", script='', onLoad=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
        self.onLoad = onLoad