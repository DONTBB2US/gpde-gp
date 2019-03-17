from tortoise import fields

from .base import BaseModel

class Role(BaseModel):
    name = fields.CharField(max_length=60)
    permissions = fields.IntField()

class Permission:
    #管理员权限
    ADMINISTER = 0x01
