from tortoise.models import Model
from tortoise import fields

class Form(Model):
    id = fields.IntField(pk=True)
    client_name = fields.CharField(max_length=300)
    client_email = fields.CharField(max_length=300)
    service_description = fields.TextField(max_length=1400)
