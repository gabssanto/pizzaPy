class Div:
    def __init__(self, className="", children={}):
        self.className = className
        self.children = children

    def __repr__(self):
        return '<div>{children}<div/>'.format(children=self.children)


print(Div(
    children=['li']
))
