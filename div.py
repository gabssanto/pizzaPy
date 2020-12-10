class Div:
    def __new__(self, className="", children={}):
        self.className = className
        self.children = children
        self.html = ''
        for child in self.children:
            self.html = self.html + child
        return '<div>{children}<div/>'.format(children=self.html)
