from fastapi import APIRouter, HTTPException
from app.db.errors import EntityNotFound

from app.schemas.product import Product
from app.db.repositories.products import ProductsRepository
from fastapi import APIRouter, Depends
from app.api.v1.dependencies.db import get_repository
router = APIRouter()


@router.get(
    "/",
    response_model=list[Product],
)
async def get_all_products(
    products_repo: ProductsRepository = Depends(get_repository(ProductsRepository))
) -> list[Product]:
    products = await products_repo.get_all_products()
    return products

@router.get(
    "/{id}",
    response_model=Product,
)
async def get_product_by_id(
    id: int,
    products_repo: ProductsRepository = Depends(get_repository(ProductsRepository))
) -> Product:
    try:
        product = await products_repo.get_product_by_id(id=id)
    except EntityNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    return product