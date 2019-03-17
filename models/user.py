from tortoise import fields
from tortoise.models import Model

from werkzeug.security import generate_password_hash

from .base import BaseModel
from .role import Role



class User(BaseModel):
    email = fields.CharField(max_length=100)
    name = fields.CharField(max_length=60)
    password = fields.CharField(max_length=60)
    active = fields.BooleanField(default=True)
    role = fields.ForeignKeyField('models.Role', related_name='users')

class UserInfo(Model):
    ...

async def create_admin(**data):
    if 'name' not in data or 'password' not in data:
        raise ValueError('name and password are required')

    data['password'] = generate_password_hash(data.pop('password'))
    #获取ADMIN Role
    r_admin = await Role.get(name='admin')
    data['role'] = r_admin
    admin = User.create(**data)
    return admin


    
