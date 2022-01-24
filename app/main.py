import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routes.api import router as api_v1_router
from app.core.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_v1_router, prefix="/v1")

    return application


app = get_application()


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
