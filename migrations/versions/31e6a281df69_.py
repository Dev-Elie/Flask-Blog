"""empty message

Revision ID: 31e6a281df69
Revises: 6bdfeebe06c5
Create Date: 2021-02-20 17:46:45.248657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e6a281df69'
down_revision = '6bdfeebe06c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('replies_ibfk_1', 'replies', type_='foreignkey')
    op.create_foreign_key(None, 'replies', 'comments', ['comment_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'replies', type_='foreignkey')
    op.create_foreign_key('replies_ibfk_1', 'replies', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###
