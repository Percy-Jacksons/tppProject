"""empty message

Revision ID: d1c70914df7d
Revises: f39d2ead13ef
Create Date: 2018-06-06 16:24:22.351031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1c70914df7d'
down_revision = 'f39d2ead13ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('nickname', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=12), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_life', sa.Boolean(), nullable=True),
    sa.Column('regist_time', sa.DateTime(), nullable=True),
    sa.Column('last_login_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_user')
    # ### end Alembic commands ###
