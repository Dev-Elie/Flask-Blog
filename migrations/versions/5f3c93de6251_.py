"""empty message

Revision ID: 5f3c93de6251
Revises: 817cc859ff16
Create Date: 2021-03-22 18:52:51.985646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3c93de6251'
down_revision = '817cc859ff16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replies', sa.Column('comment_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('replies', 'comment_id')
    # ### end Alembic commands ###