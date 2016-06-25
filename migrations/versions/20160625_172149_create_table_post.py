revision = '8161910bc1fb'
down_revision = '9b2fc1d0704a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('post',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('person_id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.Text(), nullable=False),
                    sa.Column('created_on', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['person_id'], ['person.id']),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('post')
