"""Database creat

Revision ID: a146b5a031e0
Revises: e09798ba7832
Create Date: 2023-04-14 16:45:46.117393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a146b5a031e0'
down_revision = 'e09798ba7832'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_id', table_name='user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    # ### end Alembic commands ###