from tortoise import fields
from tortoise.models import Model


class Events(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    startDate = fields.DateField()
    endDate = fields.DateField()
    latitude = fields.FloatField()
    longitude = fields.FloatField()
    imageUrl = fields.CharField(max_length=255)
    categories = fields.CharField(max_length=255)
    habitantes = fields.IntField()
