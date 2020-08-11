import sqlite3
import os
import json


#SERVERID
#   CHANNELS
#       CHANELID text
#       PRIVATE integer


def __openSDb(dbname:str):
    return sqlite3.connect(os.path.join(".","toolbox","data","Sdatabase", f"{dbname}.db"))
    
def __openDb(dbname:str):
    return sqlite3.connect(os.path.join(".","toolbox","data","database", f"{dbname}.db"))


def getTable(dbtype:str, dbname:str, table:str):
    if dbtype == "S":
        conn = __openSDb(dbname)
    if dbtype == "A":
        conn = __openDb(dbname)
    c = conn.cursor()
    try:
        c.execute(f"SELECT * FROM {table}")

        data= c.fetchall()
    except:
        data = "None"

    conn.commit()
    conn.close()
    return data

def dictTable(dbtype:str, dbname:str, table:str):
    return {key:val for key,val in getTable(dbtype,dbname, table)}

def addChannel(SERVERID:str,CHANELID:str, PRIVATE:str):
    conn = __openSDb(SERVERID)
    c = conn.cursor()
    try:
        data = {"a": CHANELID, "b": PRIVATE}
        c.execute(f"INSERT INTO stackedchannels VALUES(:a, :b)", data)
    except:
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS stackedchannels(
            chanelid text,
            private text
        )""")
        data = {"a": CHANELID, "b": PRIVATE}
        c.execute(f"INSERT INTO stackedchannels VALUES(:a, :b)", data)

    conn.commit()
    conn.close()

def removeChannel(SERVERID:str, CHANNELID:str):
    conn = __openSDb(SERVERID)
    c = conn.cursor()
    c.execute(f"DELETE FROM stackedchannels WHERE chanelid= {CHANNELID}")

    conn.commit()
    conn.close

def addActivechannel(CHANNELID:str, private:str): 
    with open(os.path.join(".","toolbox","data","database","activechannels.json"), "r") as f:
        content = json.load(f)
    content[0].append(CHANNELID)
    content[1][CHANNELID] = private
    with open(os.path.join(".", "toolbox", "data", "database", "activechannels.json"), "w") as f:
        json.dump(content, f)

def removeActivechannel(CHANNELID:str):
    with open(os.path.join(".","toolbox","data","database","activechannels.json"), "r") as f:
        content = json.load(f)
    content[0].remove(CHANNELID)
    del content[1][CHANNELID]
    with open(os.path.join(".", "toolbox", "data", "database", "activechannels.json"), "w") as f:
        json.dump(content, f)

def getActiveChannels():
    with open(os.path.join(".","toolbox","data","database","activechannels.json"), "r") as f:
        content = json.load(f)
        return content[0]

def getActiveChannelsPrivate(CHANNELID:str):
    with open(os.path.join(".","toolbox","data","database","activechannels.json"), "r") as f:
        content = json.load(f)
        content = content[1]
        return content.get(CHANNELID)
