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

from api.routes.auth_routes import (
    router as auth_router
)

from api.routes.admin_routes import (
    router as admin_router
)

from database.database import Base
from database.database import engine

from database import models
from database.ensure_rbac_schema import (
    ensure_application_schema
)

app = FastAPI(
    title="Hotel Guest Behavior Intelligence"
)

Base.metadata.create_all(
    bind=engine
)

ensure_application_schema()

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

app.include_router(
    auth_router
)

app.include_router(
    admin_router
)


@app.get("/login-page")
def login_page(
    request: Request
):

    return templates.TemplateResponse(

        request=request,

        name="login.html"
    )


@app.get("/register-page")
def register_page(
    request: Request
):

    return templates.TemplateResponse(

        request=request,

        name="register.html"
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


@app.get("/admin")
def admin_page(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="admin.html"
    )
