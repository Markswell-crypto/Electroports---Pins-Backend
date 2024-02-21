"""Add Foreign keys and relationships

Revision ID: 0d6313224785
Revises: 1618d7313f16
Create Date: 2024-02-21 09:31:30.176840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d6313224785'
down_revision = '1618d7313f16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('laptop_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('accessory_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('sound_device_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'sound_device', ['sound_device_id'], ['id'])
        batch_op.create_foreign_key(None, 'accessory', ['accessory_id'], ['id'])
        batch_op.create_foreign_key(None, 'phone', ['phone_id'], ['id'])
        batch_op.create_foreign_key(None, 'laptop', ['laptop_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('sound_device_id')
        batch_op.drop_column('accessory_id')
        batch_op.drop_column('laptop_id')
        batch_op.drop_column('phone_id')

    # ### end Alembic commands ###
