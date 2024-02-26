"""empty message

Revision ID: fa5d2a1754fc
Revises: 45246a55bff3
Create Date: 2024-02-25 22:52:55.526177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa5d2a1754fc'
down_revision = '45246a55bff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_name', sa.String(length=50), nullable=False))
        batch_op.drop_column('surname')
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('surname', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
        batch_op.drop_column('full_name')

    # ### end Alembic commands ###
