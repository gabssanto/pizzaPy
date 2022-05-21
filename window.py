from flask import url_for


class Window:
    _instance = None

    # def __new__(cls, component):
    #     if cls._instance is None:
    #         cls._instance = super(Window, cls).__new__(cls)
    #     cls.component = component
    #     return cls._instance

    def __init__(self, component):
        self.component = component

    def __repr__(self) -> str:

        return f'''
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
                <script src="{url_for('static', filename='bridge.js')}"></script>
            </head>
            <body>
                {self.component.__repr__()}
            </body>
            </html>
    '''

    def find_element_by_class(self):
        return 's'

    def writeFile(self):
        # self.a = str(pathlib.Path(__file__).parent.absolute()) + '/static/'
        # self.f = open("{a}index.html".format(a=self.a), "w+")
        # self.f.write(repr(component))
        # self.f.close()
        return repr(self.component)

# <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
# <script type=text/javascript>
#         $(function() {
#           $('a#test').on('click', function(e) {
#             e.preventDefault()
#             $.getJSON('/background_process_test',
#                 function(data) {
#               //do nothing
#             });
#             return false;
#           });
#         });
# </script>
