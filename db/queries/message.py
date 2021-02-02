from typing import List

from api.request import RequestCreateMessageDto, RequestPatchMessageDto
from db.database import DBSession
from db.exceptions import DBUserNotExistsException, DBMessageNotExistsException
from db.models import DBUser
from db.models import DBMessage


def create_message(session: DBSession, message: RequestCreateMessageDto, converse_id: dict) -> DBMessage:
    new_message = DBMessage(
        message=message.message,
        sender_id=converse_id.get('sender_id'),
        recipient_id=converse_id.get('recipient_id')
    )

    session.add_model(new_message)

    return new_message


def get_user(session: DBSession, *, login: str = None, user_id: int = None) -> DBUser:
    db_user = None

    if login is not None:
        db_user = session.get_user_by_login(login)
    elif user_id is not None:
        db_user = session.get_user_by_id(user_id)

    if db_user is None:
        raise DBUserNotExistsException
    return db_user


def get_messages(session: DBSession, user_id: int) -> List['DBMessage']:
    return session.get_incoming_messages(user_id)


def get_dialog(session: DBSession, sender_id: int, recipient_id: int) -> List['DBMessage']:
    db_dialog_messages = session.get_dialog_message(sender_id=sender_id, recipient_id=recipient_id)

    if not db_dialog_messages:
        raise DBMessageNotExistsException
    return db_dialog_messages


def patch_message(
        session: DBSession, message: RequestPatchMessageDto, user_id: int, message_id: int
) -> DBMessage:

    db_message = session.get_message_by_id(user_id=user_id, message_id=message_id)

    if db_message is None:
        raise DBMessageNotExistsException

    for attr in message.fields:
        setattr(db_message, attr, getattr(message, attr))

    return db_message


def delete_message(session: DBSession, user_id: int, message_id: int) -> DBMessage:

    db_message = session.get_message_by_id(user_id=user_id, message_id=message_id)

    if db_message is None:
        raise DBMessageNotExistsException

    db_message.is_deleted = True

    return db_message


def get_message(session: DBSession, *, user_id: id, message_id: int) -> DBMessage:

    db_message = session.get_message_by_id(user_id=user_id, message_id=message_id)

    if db_message is None:
        raise DBMessageNotExistsException

    return db_message
