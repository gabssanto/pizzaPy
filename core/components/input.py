from core.components.base_component import BaseComponent


class Input(BaseComponent):
    def __init__(self, className="", src=""):
        self.className = className
        self.src = src

    def __repr__(self) -> str:
        return self.mount_self_closing_component('input')
