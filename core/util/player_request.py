from core.model.player import Player
import mysql.connector
import logging

odyssia_db = mysql.connector.connect(
    host="185.157.246.189",
    user="odyssia_admin",
    password="LF[#S2je",
    database="odyssia"
)
logging.info(odyssia_db.is_connected())


def getStats(player_name: str):
    cursor = odyssia_db.cursor()

    # if the connection was lost, then it reconnects
    odyssia_db.ping(reconnect=True)

    cursor.execute(f"SELECT game_points, top1, kills, deaths FROM stats WHERE player_id = '{getPlayerID(player_name)}'")

    result = cursor.fetchall()[0]
    return Player("?", player_name, result[0], result[1], result[2], result[3])


def getPlayerID(player_name: str):
    cursor = odyssia_db.cursor()
    cursor.execute(f"SELECT id FROM players WHERE name = '" + player_name + "'")

    result = cursor.fetchall()
    for data in result:
        return data[0]



