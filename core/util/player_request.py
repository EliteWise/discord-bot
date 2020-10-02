from core.model.player import Player
import mysql.connector
import logging
import settings

odyssia_db = mysql.connector.connect(
    host=settings.HOSTNAME,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    database="odyssia"
)
logging.info(odyssia_db.is_connected())


def getStats(player_name: str):

    # if the connection was lost, then it reconnects
    if odyssia_db.is_connected() == False:
        logging.info("Try to reconnect...")
        odyssia_db.reconnect(attempts=3)

    cursor = odyssia_db.cursor()

    cursor.execute(f"SELECT game_points, top1, kills, deaths FROM stats WHERE player_id = '{getPlayerID(player_name)}'")

    result = cursor.fetchall()[0]
    return Player("?", player_name, result[0], result[1], result[2], result[3])


def getPlayerID(player_name: str):
    cursor = odyssia_db.cursor()
    cursor.execute(f"SELECT id FROM players WHERE name = '" + player_name + "'")

    result = cursor.fetchall()
    for data in result:
        return data[0]



