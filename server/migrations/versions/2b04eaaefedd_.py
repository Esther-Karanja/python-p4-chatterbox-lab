"""empty message

Revision ID: 2b04eaaefedd
Revises: caa29d9999b7
Create Date: 2023-12-07 13:25:50.752392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b04eaaefedd'
down_revision = 'caa29d9999b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('message_body', sa.String(), nullable=True))
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.VARCHAR(), nullable=True))
    op.drop_column('messages', 'message_body')
    # ### end Alembic commands ###
