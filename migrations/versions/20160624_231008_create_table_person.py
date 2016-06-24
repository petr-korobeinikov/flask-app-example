revision = '9b2fc1d0704a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('person',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=True),
                    sa.Column('username', sa.String(length=40), nullable=True),
                    sa.Column('password', sa.String(length=60), nullable=True),
                    sa.Column('created_on', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )


def downgrade():
    op.drop_table('person')
