from starlette.applications import Starlette
from starlette.routing import Route

from app.api.routes.web_template import home

routes = [
    Route('/', endpoint=home)
]

app = Starlette(debug=True, routes=routes)
