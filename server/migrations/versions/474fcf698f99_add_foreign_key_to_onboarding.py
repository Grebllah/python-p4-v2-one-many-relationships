"""add foreign key to onboarding

Revision ID: 474fcf698f99
Revises: 7ac93369b047
Create Date: 2024-04-15 16:47:01.651006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '474fcf698f99'
down_revision = '7ac93369b047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.create_foreign_key(
            "employee_id",
            "onboardings",
            ["employee_id"],
            ["id"],
        )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
     with op.batch_alter_table('onboardings', schema=None) as batch_op:
        op.drop_column("employee_id")
