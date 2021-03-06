"""empty message

Revision ID: b04678e62e00
Revises: 66ce08517edd
Create Date: 2021-02-19 12:46:26.892117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b04678e62e00'
down_revision = '66ce08517edd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('replies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=2000), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_replies_date_posted'), 'replies', ['date_posted'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_replies_date_posted'), table_name='replies')
    op.drop_table('replies')
    # ### end Alembic commands ###
