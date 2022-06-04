from flask import url_for

class Window:
    _instance = None

    def __init__(self, element, title='Pizza Py'):
        self.element = element
        self.title = title

    def __repr__(self) -> str:
        return f'''
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{self.title}</title>
                <!-- <link rel="stylesheet" href="{url_for('static', filename='pyscript.css')}" /> -->
                <script defer type="text/javascript" src="{url_for('static', filename='pyscript.js')}"></script>
            </head>
            <body>
                <py-env>
                - paths:
                    - ./static/components.py
                </py-env>
                <div id="root"></div>
                <py-script src="{url_for('static', filename='renderer.py')}"></py-script>
                <py-script src="{url_for('static', filename='index.py')}"></py-script>
            </body>
            </html>
    '''