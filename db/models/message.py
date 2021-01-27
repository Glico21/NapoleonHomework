from sqlalchemy import Column, Integer, VARCHAR, BOOLEAN

from db.models import BaseModel


class DBMessage(BaseModel):

    __tablename__ = 'messages'

    message = Column(VARCHAR(280), nullable=True)
    sender_id = Column(Integer, nullable=False)
    recipient_id = Column(Integer, nullable=False)
    is_deleted = Column(BOOLEAN, nullable=False, default=False)
