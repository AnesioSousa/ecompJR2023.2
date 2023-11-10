from tortoise import Model, fields
from datetime import datetime

class User(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=300)
    email = fields.CharField(max_length=300)
    password = fields.CharField(max_length=300)
    created_at = fields.DatetimeField(defaut=datetime.now(), auto_now_add=True)

    class Meta:
        ordering=["name"]
    