from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def home(request):
    return JSONResponse({
        "message":"Hello How are you"
    })
    
routes = [Route("/", endpoint=home)]

app=Starlette(debug=True, routes=routes)