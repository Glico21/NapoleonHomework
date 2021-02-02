from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, Session, Query

from db.exceptions import DBIntegrityException, DBDataException
from db.models import BaseModel, DBUser, DBMessage


class DBSession:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def query(self, *args, **kwargs) -> Query:
        return self._session.query(*args, **kwargs)

    def avaiable_users(self) -> Query:
        return self.query(DBUser).filter(DBUser.is_deleted.isnot(True))

    def unavaiable_users(self) -> Query:
        return self.query(DBUser).filter(DBUser.is_deleted.isnot(False))

    def add_model(self, model: BaseModel):
        try:
            self._session.add(model)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

    def get_user_by_login(self, login: str) -> DBUser:
        return self.avaiable_users().filter(DBUser.login == login).first()

    def get_user_by_id(self, uid: int) -> DBUser:
        return self.avaiable_users().filter(DBUser.id == uid).first()

    def get_deleted_user_by_login(self, login: str) -> DBUser:
        return self.unavaiable_users().filter(DBUser.login == login).first()

    def get_user_all(self) -> List[DBUser]:
        qs = self.avaiable_users()
        return qs.all()

    def messages(self) -> Query:
        return self.query(DBMessage).filter(DBMessage.is_deleted.isnot(True))

    def incoming_messages(self, user_id) -> Query:
        return self.messages().filter(DBMessage.recipient_id == user_id)

    def outgoing_messages(self, user_id) -> Query:
        return self.messages().filter(DBMessage.sender_id == user_id)

    def get_message_by_id(self, user_id, message_id) -> DBMessage:
        return self.outgoing_messages(user_id).filter(DBMessage.id == message_id).first()

    def get_incoming_messages(self, user_id: int) -> List[DBMessage]:
        return self.incoming_messages(user_id).all()

    def get_dialog_message(self, sender_id: int, recipient_id: int) -> List[DBMessage]:
        incoming = self.incoming_messages(user_id=sender_id).filter(DBMessage.sender_id == recipient_id)
        outgoing = self.outgoing_messages(user_id=sender_id).filter(DBMessage.recipient_id == recipient_id)
        return incoming.union(outgoing).all()

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

        if need_close:
            self.close_session()

    def close_session(self):
        self._session.close()


class DataBase:
    connection: Engine
    session_factory: sessionmaker
    _test_query = 'SELECT 1'

    def __init__(self, connection: Engine):
        self.connection = connection
        self.session_factory = sessionmaker(bind=self.connection)

    def check_connection(self):
        self.connection.execute(self._test_query).fetchone()

    def make_session(self) -> DBSession:
        session = self.session_factory()
        return DBSession(session)
