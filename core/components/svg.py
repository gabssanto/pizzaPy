from core.components.base_component import BaseComponent


class Svg(BaseComponent):
    def __init__(self, className="", children=[]):
        super().__init__()
        self.className = className
        self.children = children

    def __repr__(self) -> str:
        return self.mount_children_component('svg')