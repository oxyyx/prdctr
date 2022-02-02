from app.db.errors import EntityNotFound
from app.db.repositories.base import BaseRepository
from app.schemas.product import Product

class ProductsRepository(BaseRepository):
    async def get_product_by_id(self, *, id: int) -> Product:
        """
        Get unique product by ID
        """
        product = await self.connection.fetchrow(
            'select id, slug, description from products where id = $1',
            id
        )

        if product:
            return Product(**dict(product))

        raise EntityNotFound(f"Product with ID {id} not found.")

    async def get_all_products(self) -> list[Product]:
        """
        Get all products stored in the database.
        """
        products = []

        async with self.connection.transaction():
            async for record in self.connection.cursor('select id, slug, description from products'):
                if record is None or len(record) == 0:
                    break

                product = Product(**dict(record))
                
                products.append(product)

        return products