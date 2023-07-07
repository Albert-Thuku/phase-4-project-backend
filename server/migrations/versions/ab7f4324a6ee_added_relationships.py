"""Added relationships

Revision ID: ab7f4324a6ee
Revises: b379fce7498a
Create Date: 2023-07-07 08:19:17.024675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab7f4324a6ee'
down_revision = 'b379fce7498a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('centres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(length=10), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adoptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('animal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('centre_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'centres', ['centre_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('centre_id')

    op.drop_table('adoptions')
    op.drop_table('users')
    op.drop_table('centres')
    # ### end Alembic commands ###