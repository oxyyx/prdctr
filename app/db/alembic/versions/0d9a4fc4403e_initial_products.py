"""Initial products

Revision ID: 0d9a4fc4403e
Revises: 
Create Date: 2022-01-24 21:25:18.654549

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0d9a4fc4403e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("slug", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_products_id"), "products", ["id"], unique=True)
    op.create_index(op.f("ix_products_slug"), "products", ["slug"], unique=True)


def downgrade():
    op.drop_table("products")
