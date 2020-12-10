from div import Div


class Component:
    def __new__(self):
        return Div(children=['hello', Div(children=['world'])])


print(Component())
