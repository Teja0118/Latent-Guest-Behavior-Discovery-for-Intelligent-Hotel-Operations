'''
from fastapi import FastAPI

from api.routes.prediction_routes import (
    router as prediction_router
)

app = FastAPI(
    title=(
        "Latent Guest Behavior Discovery API"
    )
)

app.include_router(prediction_router)

@app.get("/")
def root():
    return {
        "message": (
            "Hotel Guest Behavior API Running"
        )
    }
'''