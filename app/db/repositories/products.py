from app.db.errors import EntityNotFound
from app.db.repositories.base import BaseRepository
from app.schemas.product import Product

class ProductsRepository(BaseRepository):
    async def get_product_by_id(self, *, id: int) -> Product:
        product = await self.connection.fetchrow(
            'select slug, description from products where id = $1',
            id
        )

        if product:
            return Product(**dict(product))

        raise EntityNotFound(f"Product with ID {id} not found.")

    async def get_all_products(self) -> list[Product]:
        products = []

        while True:
            product = await self.connection.fetch('select slug, description from products')

            if product is None:
                break
            
            products.append(Product(**dict(product)))

        return products