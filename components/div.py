class Div:
    def parseKey(self, key: str) -> str:
        # print('key ' + key)
        if key == 'backgroundColor':
            return 'background-color'
        return key

    def mountStyle(self, style: dict) -> str:
        string = ''
        for key in style:
            string += self.parseKey(key) + ':' + style[key] + ';'
        return string

    def __repr__(self) -> str:
        for child in self.children:
            self.html = self.html + str(child)

        string = '<div'

        if self.className != '':
            string += ' class="' + self.className + '"'

        if self.style != '':
            string += ' style="' + self.style + '"'

        if self.onClick != '':
            string += ' onclick="() => ' + str(self.onClick) + '"'

        string += '>' + self.html + '</div>' + self.script
        return string

    def __init__(self, className="", children={}, style={}, onClick="", script=''):
        self.className = className
        self.children = children
        self.style = self.mountStyle(style)
        self.onClick = onClick
        self.script = script
        self.html = ''

        # print(self.onClick, 'here')

        # for child in self.children:
        #     self.html = self.html + child

        # string = '<div'

        # if self.className != '':
        #     string += ' class="' + self.className + '"'

        # if self.style != '':
        #     string += ' style="' + self.style + '"'

        # if self.onClick != '':
        #     string += ' onclick="' + self.onClick + '"'

        # string += '>' + self.html + '</div>'
        # return string
        # return '<div class={className} style={style} >{children}</div>'.format(children=self.html,
        #                                                                        className=self.className,
        #                                                                        style=self.style)

# TODO: implement div via JS
# string = ''

#         string += 'var div = document.createElement("DIV");' + \
#             'div.innerText = "{children}";'.format(children=self.html) + \
#             'document.body.appendChild(div);'
