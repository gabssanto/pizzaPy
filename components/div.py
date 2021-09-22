class Div:
    def parseKey(key: str) -> str:
        print('key ' + key)
        if key == 'backgroundColor':
            return 'background-color'
        return ''

    def mountStyle(self, style: dict) -> str:
        string = ''
        for key in style:
            string += self.parseKey(key) + ':' + style[key] + ';'
        return string

    def __new__(self, className="", children={}, style={'backgroundColor': 'red'}):
        self.className = className
        self.children = children
        self.style = self.mountStyle(self, style)
        self.onClick = ''
        self.html = ''

        for child in self.children:
            self.html = self.html + child

        string = '<div'

        if self.className != '':
            string += ' class="' + self.className + '"'

        if self.style != '':
            string += ' style="' + self.style + '"'

        if self.onClick != '':
            string += ' onclick="' + self.onClick + '"'

        string += '>' + self.html + '</div>'
        return string
        # return '<div class={className} style={style} >{children}</div>'.format(children=self.html,
        #                                                                        className=self.className,
        #                                                                        style=self.style)

# TODO: implement div via JS
# string = ''

#         string += 'var div = document.createElement("DIV");' + \
#             'div.innerText = "{children}";'.format(children=self.html) + \
#             'document.body.appendChild(div);'
