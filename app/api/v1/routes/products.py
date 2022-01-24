from fastapi import APIRouter

from app.schemas.product import Product

router = APIRouter()


@router.get(
    "/",
    response_model=list[Product],
)
async def get_all_products(
) -> list[Product]:
    products = []
    return products
