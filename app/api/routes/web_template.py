from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='app/views/templates')


def home(request):
    return templates.TemplateResponse('index.html', {'request': request, 'response': {'title': 'Home'}})
