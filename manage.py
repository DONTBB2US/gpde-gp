import click

from tortoise import Tortoise, run_async
from tortoise.exceptions import IntegrityError

from ext import init_db
from models.user import create_admin
from models.role import Role

async def init():
    await init_db(create_db=False)
    await Tortoise._drop_databases()
    await init_db(create_db=True)
    await Tortoise.generate_schemas()

    await init_role_table()

async def init_role_table():
    role_map = {
        'admin', '1'
    }
    for n, p in role_map:
        await Role.create(name=n, permissions=p)

@click.group()
def cli():
    ...

@cli.command()
def initdb():
    run_async(init())
    click.echo('Init Finished!')


async def _add_admin(**kwargs):
    await init_db()
    try:
        admin = await create_admin(**kwargs)
    except IntegrityError as e:
        click.echo(str(e))
    else:
        click.echo(f'Admin {admin.name} created!!! ID: {admin.id}')

@cli.command()
@click.option('--name', required=True, prompt=True)
@click.option('--email', required=True, default=None, prompt=True)
@click.option('--password', required=True, prompt=True, hide_input=True,
              confirmation_prompt=True)
def adduser(name, email, password):
    run_async(_add_admin(name=name, password=password, email=email))


if __name__ == '__main__':
    cli()