"""empty message

Revision ID: 7f72b880ab28
Revises: 1fe0ac25964d
Create Date: 2024-09-27 14:57:02.208904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f72b880ab28'
down_revision = '1fe0ac25964d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('repassword', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('repassword')

    # ### end Alembic commands ###
