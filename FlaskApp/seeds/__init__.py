from flask.cli import AppGroup
from .members import seed_members
from .users import seed_users
from .clubs import seed_clubs
from .restaurants import seed_restaurants

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_clubs()
    seed_members()
    seed_restaurants()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_members()
    undo_clubs()
