from sqlalchemy import Column, VARCHAR, LargeBinary, Boolean

from db.models import BaseModel


class DBUser(BaseModel):

    __tablename__ = 'users'

    login = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(LargeBinary(), nullable=False)
    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    is_deleted = Column(Boolean, default=False)
