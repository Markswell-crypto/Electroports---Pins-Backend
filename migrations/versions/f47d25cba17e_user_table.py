"""user table

Revision ID: f47d25cba17e
Revises: 25704466bfd0
Create Date: 2024-02-18 18:22:22.939720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f47d25cba17e'
down_revision = '25704466bfd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=60), nullable=False))
        batch_op.create_unique_constraint('uq_username', ['username'])
        batch_op.create_unique_constraint('uq_email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('uq_email', type_='unique')
        batch_op.drop_constraint('uq_username', type_='unique')
        batch_op.drop_column('password')
        batch_op.drop_column('email')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
