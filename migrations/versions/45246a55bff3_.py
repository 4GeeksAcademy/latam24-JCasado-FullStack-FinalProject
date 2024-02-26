"""empty message

Revision ID: 45246a55bff3
Revises: 676f15700d52
Create Date: 2024-02-25 22:49:07.594293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45246a55bff3'
down_revision = '676f15700d52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
