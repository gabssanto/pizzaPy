import base64
from io import BytesIO
from core.components.img import Img
from core.components.svg import Svg

from flask import Flask
from matplotlib.figure import Figure


from core.components.div import Div


# Generate the figure **without using pyplot**.
fig = Figure()
ax = fig.subplots()
ax.plot([1, 2])
# Save it to a temporary buffer.
buf = BytesIO()
fig.savefig(buf, format="png")
# Embed the result in the html output.
data = base64.b64encode(buf.getbuffer()).decode("ascii")

def matplotlibPage():

    return Div(
        children=[
            "Hello world",
            Img(src="data:image/png;base64,{}".format(data)),
            Svg(children=[
                '<circle cx="100" cy="100" r="50" fill="red" />'
            ])
        ]
    )