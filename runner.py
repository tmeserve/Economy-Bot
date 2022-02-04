import discord, util
from discord.ext import commands
from interactions.models.command import ApplicationCommand
from pymongo import MongoClient
from constants import set_database, set_collection

discord_client = commands.Bot(command_prefix=">.<", Intents=discord.Intents.default())

@discord_client.event
async def on_ready():
    print("Logged in as")
    print(discord_client.user.name)
    print(discord_client.user.id)

if __name__ == '__main__':
    secrets = util.load_secrets()
    
    disc_token = secrets['discord']['token']
    ip = secrets['database']['IP']
    port = secrets['database']['port']
    username = secrets['database']['username']
    password = secrets['database']['password']
    databaseStr = secrets['database']['database']
    collectionStr = secrets['database']['collection']

    slash = ApplicationCommand(discord_client, override_type=True, sync_commands=True)
    uri = f'mongodb://{username}:{password}@{ip}:{port}/'
    mongo_client = MongoClient(uri)

    if not (databaseStr in mongo_client.list_database_names()):
        database = mongo_client[databaseStr]
    else:
        database = mongo_client.get_database(databaseStr)
    set_database(database)

    if not (collectionStr in database.list_collection_names()):
        collection = database[collectionStr]
    else:
        collection = mongo_client.get_database(databaseStr)
    set_collection(collection)

    discord_client.load_extension("cogs.commands.balance")
    discord_client.load_extension("cogs.commands.leaderboard")
    discord_client.load_extension("cogs.commands.money")

    discord_client.run(disc_token)
