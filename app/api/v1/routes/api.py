from fastapi import APIRouter

from app.api.v1.routes import products

router = APIRouter()

router.include_router(products.router, tags=["Products"], prefix="/products")
