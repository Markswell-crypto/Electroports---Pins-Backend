"""Add logo_url column to Brand model

Revision ID: 13074c4609fa
Revises: 5a1263fccd78
Create Date: 2024-02-15 12:04:30.555444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13074c4609fa'
down_revision = '5a1263fccd78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accessory', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    with op.batch_alter_table('brand', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo_url', sa.String(length=255), nullable=True))

    with op.batch_alter_table('laptop', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    with op.batch_alter_table('phone', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    with op.batch_alter_table('sound_device', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sound_device', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    with op.batch_alter_table('phone', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    with op.batch_alter_table('laptop', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    with op.batch_alter_table('brand', schema=None) as batch_op:
        batch_op.drop_column('logo_url')

    with op.batch_alter_table('accessory', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
