from core.components.base_component import BaseComponent


class Img(BaseComponent):
    def __init__(self, className="", src=""):
        self.className = className
        self.src = src

    # Build the component based on this doc: https://matplotlib.org/3.1.0/faq/howto_faq.html#:~:text=Matplotlib%20is%20not%20thread%2Dsafe,serialize%20access%20to%20Matplotlib%20artists.
    def __repr__(self) -> str:
        return self.mount_self_closing_component('img')