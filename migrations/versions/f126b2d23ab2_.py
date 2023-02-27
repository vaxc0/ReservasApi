"""empty message

Revision ID: f126b2d23ab2
Revises: 2fb74f4256c6
Create Date: 2023-02-26 17:28:05.398468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f126b2d23ab2'
down_revision = '2fb74f4256c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hora_realizada', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('fecha_reservar', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('hora_reservar', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('hora_finalReservar', sa.String(), nullable=True))
        batch_op.drop_column('fecha_vencimiento')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fecha_vencimiento', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('hora_finalReservar')
        batch_op.drop_column('hora_reservar')
        batch_op.drop_column('fecha_reservar')
        batch_op.drop_column('hora_realizada')

    # ### end Alembic commands ###
