from app.schemas.base import Base
from app.schemas.mixins import IDModelMixin, AuditedModelMixin


class Product(IDModelMixin, Base, AuditedModelMixin):
    slug: str
    description: str
