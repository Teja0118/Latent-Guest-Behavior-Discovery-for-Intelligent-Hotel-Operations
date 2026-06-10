from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from fastapi.requests import Request

from api.routes.prediction_routes import (
    router as prediction_router
)

from api.routes.analytics_routes import (
    router as analytics_router
)

app = FastAPI(
    title="Hotel Guest Behavior Intelligence"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)

app.include_router(
    prediction_router
)

app.include_router(
    analytics_router
)


@app.get("/")
def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/predict")
def predict_page(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="predict.html"
    )


@app.get("/analytics")
def analytics_page(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="analytics.html"
    )


@app.get("/history")
def history_page(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="history.html"
    )


@app.get("/about")
def about_page(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )