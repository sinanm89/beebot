# Work with Python 3.6
import discord
import os
import requests

TOKEN = os.environ.get('CLIENT_ID', '553390519997169665')
SECRET = os.environ.get('CLIENT_SECRET', '0vbnP0LGEYNhtIXbzG8WaVgwoVlhbj3_')
REDIRECT_URI = "https://rahatol.com"
urls = {
    'auth': "https://discordapp.com/api/oauth2/authorize",
    'token': "https://discordapp.com/api/oauth2/token",
    'revoke': "https://discordapp.com/api/oauth2/token/revoke",
    'api': 'https://discordapp.com/api/v6',
}

# def exchange_code():
#     auth_url= "https://discordapp.com/api/oauth2/token"
#     scopes = [
#         "identify", "email","guilds", "connections", "guilds.join","gdm.join", "webhook.incoming","rpc.notifications.read",
#         "rpc.api", "bot", "rpc", "messages.read", "applications.builds.upload", "applications.builds.read",
#         "applications.store.update", "applications.entitlements"]
#     data = {
#     "client_id": TOKEN,
#     "client_secret": SECRET,
#     "permissions": "8",
#     "redirect_uri": "https://beebot.rahatol.com/auth",
#     "response_type": "code",
#     "scope": " ".join(scopes)
#     }
#     headers = {
#     'Content-Type': 'application/x-www-form-urlencoded'
#     }

#     r = requests.post(auth_url, data=data, headers=headers)

#     import ipdb; ipdb.set_trace()
#     r.raise_for_status()
#     return r.json()

# @client.event
# async def on_message(message):
#     if message.content.startswith('$start'):
#         await client.send_message(message.channel, 'Type $stop 4 times.')
#         for i in range(4):
#             msg = await client.wait_for_message(author=message.author, content='$stop')
#             fmt = '{} left to go...'
#             await client.send_message(message.channel, fmt.format(3 - i))

#         await client.send_message(message.channel, 'Good job!')
# Advanced filters using check:

# @client.event
# async def on_message(message):
#     if message.content.startswith('$cool'):
#         await client.send_message(message.channel, 'Who is cool? Type $name namehere')

#         def check(msg):
#             return msg.content.startswith('$name')

#         message = await client.wait_for_message(author=message.author, check=check)
#         name = message.content[len('$name'):].strip()
#         await client.send_message(message.channel, '{} is cool indeed'.format(name))
# s
# # @client.event
# # async def on_message(message):
# #     if message.content.startswith('$react'):
# #         msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')

# #         def check(reaction, user):
# #             e = str(reaction.emoji)
# #             return e.startswith(('👍', '👎'))

# #         res = await client.wait_for_reaction(message=msg, check=check)
# #         await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))

# =======================================================================================================
# await client.create_channel(server, 'Voice', type=discord.ChannelType.voice)
# Creating a ‘secret’ text channel:

# everyone_perms = discord.PermissionOverwrite(read_messages=False)
# my_perms = discord.PermissionOverwrite(read_messages=True)

# everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
# mine = discord.ChannelPermissions(target=server.me, overwrite=my_perms)
# await client.create_channel(server, 'secret', everyone, mine)
# Or in a more ‘compact’ way:

# everyone = discord.PermissionOverwrite(read_messages=False)
# mine = discord.PermissionOverwrite(read_messages=True)
# await client.create_channel(server, 'secret', (server.default_role, everyone), (server.me, mine))
# =======================================================================================================


# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         await client.send_message(message.channel, msg)

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

API_ENDPOINT = 'https://discordapp.com/api/v6'
CLIENT_ID = TOKEN
CLIENT_SECRET = SECRET
REDIRECT_URI = 'https://beebot.rahatol.com/auth'

def refresh_token(refresh_token):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token,
    'redirect_uri': REDIRECT_URI,
    'scope': 'identify email connections'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data, headers)
  r.raise_for_status()
  return r.json()


def main():
    # exchange_code()

    client = discord.Client()

    @client.event
    async def on_message(message):
        if message.content.startswith('$greet'):
            await client.send_message(message.channel, 'Say hello')
            msg = await client.wait_for_message(author=message.author, content='hello')
            await client.send_message(message.channel, 'Hello.')

    client.login(TOKEN)
    import ipdb; ipdb.set_trace()
    client.run(TOKEN)

if __name__ == '__main__':
    main()
