from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from fastapi.requests import Request

from api.routes.prediction_routes import (
    router as prediction_router
)

app = FastAPI(
    title="Hotel Guest Behavior Intelligence"
)

# Static Files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Templates
templates = Jinja2Templates(
    directory="templates"
)

# API Routes
app.include_router(
    prediction_router
)

# Frontend Route
@app.get("/")
def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )