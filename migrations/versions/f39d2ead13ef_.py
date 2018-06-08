"""empty message

Revision ID: f39d2ead13ef
Revises: 
Create Date: 2018-06-06 13:49:46.809072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f39d2ead13ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_letter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parentId', sa.Integer(), nullable=True),
    sa.Column('regionName', sa.String(length=30), nullable=True),
    sa.Column('cityCode', sa.Integer(), nullable=True),
    sa.Column('pinYin', sa.String(length=50), nullable=True),
    sa.Column('letter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['letter_id'], ['t_letter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_city')
    op.drop_table('t_letter')
    # ### end Alembic commands ###
