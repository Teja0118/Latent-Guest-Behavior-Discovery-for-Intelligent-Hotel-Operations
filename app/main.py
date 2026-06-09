from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from fastapi.requests import Request

from api.routes.prediction_routes import (
    router as prediction_router
)

from database.database import engine

from database.models import Base


Base.metadata.create_all(
    bind=engine
)

app = FastAPI(

    title="Hotel Guest Behavior Intelligence System",

    description=(
        "AI-powered hospitality guest "
        "behavior clustering and "
        "recommendation system."
    ),

    version="1.0.0"
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
    prediction_router,
    tags=["Prediction API"]
)

@app.get("/health")
def health_check():

    return {

        "status": "healthy",

        "application":
            "Hotel Guest Behavior Intelligence"
    }

@app.get("/")
def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )