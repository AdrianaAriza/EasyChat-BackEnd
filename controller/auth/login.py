
from fastapi import HTTPException, status, Header
from ext.db_connection import users_collection, session_store
import bcrypt
from .schemas import LoginBase
from utils.auth import generate_session, validate_user


def login(user: LoginBase):
    user_dict = users_collection.find_one({'email': user.email})
    if user_dict:
        hashed_password = user_dict['password'].encode('utf-8')
        if bcrypt.checkpw(user.password.encode('utf-8'), hashed_password):
            token = generate_session(user_dict)
            return {'access_token': token, 'token_type': 'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")


def logout(authorization: str = Header(None)):
    user_dict = validate_user(authorization)
    session_store.delete_one({'user_id': user_dict['id']})
    return {'success': True}

