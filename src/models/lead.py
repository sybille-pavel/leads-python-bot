from tortoise.models import Model
from tortoise import fields


class LeadModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    contact = fields.CharField(max_length=100)
    product = fields.CharField(max_length=100)
    time = fields.CharField(max_length=50)