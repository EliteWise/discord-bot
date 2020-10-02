import asyncio

from mcstatus import MinecraftServer

ports = {
            'Hub': '25564',
            'Arcade': '25568',
            'Dungeon': '25569',
            'Desert': '25570',
            'Mars': '25571',
            'Poseidon': '25572'
        }

messages = []


async def update_status(channel, hostname, sleep_time):
    """
    :param channel: Channel where messages will be written
    :param hostname: IP of the server
    :param sleep_time: Time to wait before update
    :return: Send messages or edit them if they are already sent
    """

    already_send = False
    iterate = 0
    while True:
        # Using mcstatus module to get servers infos easily
        response = MinecraftServer.lookup(f'{hostname}')
        query = response.query()
        status = response.status()
        display_announcement: str = "Les serveurs Odyssia sont **accessibles à tous** !"
        display_players: str = f"Joueurs actuellement en ligne ({status.players.online}) " + (": {0}".format(", ".join(query.players.names)))
        display_status: str = "Le serveur {0} est **Ouvert**"
        separator: str = "======================"
        if already_send is False:
            # Send messages once
            await channel.send(display_announcement)
            await channel.send(separator)
            players_online = await channel.send(display_players)
            await channel.send(separator)
        else:
            # The message is edited the rest of the time, because it is already written
            await players_online.edit(content=display_players)
        for server_name, port in ports.items():
            try:
                response = MinecraftServer.lookup(f'{hostname}:{port}')
                status = response.status()
                if already_send is False:
                    # Send the message once
                    status_message = await channel.send(display_status.format(server_name, status.players.online))
                    messages.append(status_message)
                else:
                    # The message is edited the rest of the time, because it is already written
                    await messages[iterate].edit(content=display_status.format(server_name, status.players.online))
            except (ConnectionRefusedError, AttributeError, Exception):
                await messages[iterate].edit(content="Le serveur {0} est **Fermé**".format(server_name, status.players.online))
            iterate += 1
            # Wait until the next update
        await asyncio.sleep(sleep_time)
        # All messages have been sent one time, so we don't want to rewrite them, but just editing them
        already_send = True
        iterate = 0