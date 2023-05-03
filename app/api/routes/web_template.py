from starlette.responses import PlainTextResponse


def home(request):
    return PlainTextResponse('Hello, world!')
