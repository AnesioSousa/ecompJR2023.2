from tortoise import Model, fields
from datetime import datetime
from models.user.UserModel import User
        
class Token(Model):
    id = fields.IntField(pk=True, index=True)
    access_token: fields.CharField(max_length=200)
    token_type: fields.CharField(max_length=50)
    created_at = fields.DatetimeField(defaut=datetime.now(), auto_now_add=True)
    
    class Meta:
        ordering=["id"]


class TokenData(Model):
    email: str | None = None


class UserInDB(User):
    hashed_password: str