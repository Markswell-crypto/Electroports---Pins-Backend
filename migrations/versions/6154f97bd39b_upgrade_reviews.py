"""Upgrade reviews

Revision ID: 6154f97bd39b
Revises: 452149dc9393
Create Date: 2024-02-24 20:49:00.584854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6154f97bd39b'
down_revision = '452149dc9393'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_constraint('review_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('rating')
        batch_op.drop_column('component_type')
        batch_op.drop_column('component_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('component_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('component_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('review_user_id_fkey', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
