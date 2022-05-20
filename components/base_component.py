class BaseComponent:
    """
    Base class for all components.
    """

    def parseKey(self, key: str) -> str:
        if key == 'backgroundColor':
            return 'background-color'
        return ''

    def mountStyle(self, style: dict) -> str:
        string = ''
        for key in style:
            string += self.parseKey(key) + ':' + style[key] + ';'
        return string
