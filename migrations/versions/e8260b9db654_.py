"""empty message

Revision ID: e8260b9db654
Revises: d34791a2044d
Create Date: 2020-10-21 11:31:07.703326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8260b9db654'
down_revision = 'd34791a2044d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('category', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'category')
    # ### end Alembic commands ###