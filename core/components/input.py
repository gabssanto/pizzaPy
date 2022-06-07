from core.components.base_component import BaseComponent


class Input(BaseComponent):
    def __repr__(self) -> str:
        return self.mount_self_closing_component('input')
        
    def __init__(self, className="", children={}, style={}, onClick="", script='', onLoad='', onChange=""):
        self.className = className
        self.children = children
        self.onChange = onChange
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
        self.onLoad = onLoad