from core.components.base_component import BaseComponent
from core.router import RouterNavigate
from core.hooks.state import State


class Button(BaseComponent):
    def __repr__(self) -> str:
        return self.mount_children_component("button")

    def __init__(self, className="", children={}, style={}, onClick="", script=''):
        super().__init__()
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''
