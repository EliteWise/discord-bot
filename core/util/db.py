import sqlite3
import os
import json


#SERVERID
#   CHANNELS
#       CHANELID text
#       PRIVATE integer
#   VOTES
#       VOTEMESSAGEID int
#       VOTESDICTIONNARY dict


def __openDb(dbname:str):
    """

    Args:
        dbname (str): name of the database

    Returns:
        conn ection:  connection to the specified database in the server folder
    """
    return sqlite3.connect(os.path.join(".","core","database", f"{dbname}.db"))


def getTable(dbname:str, table:str, arguments= " "):
    """Get a table

    Args:
        dbname (str): the name of the database
        table (str): the name of the table

    Returns:
        table: the table
    """
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

def dictTable(dbname:str, table:str):
    """

    Args:
        dbname (str): the name of the database
        table (str): the name of the table

    Returns:
        dictionnary: return the specified table at dictionnary format
    """
    return {key:val for key,val in getTable(dbname, table)}

def writeVotes(ADMINMESSAGEID:str, Votes:dict):
    with open(os.path.join(".","core","data","votes_categories.json"), "r") as f:
        content = json.load(f)
    content[ADMINMESSAGEID] = Votes
    with open(os.path.join(".", "core", "data", "votes_categories.json"), "w") as f:
        json.dump(content, f)

def createVote(SERVERID:str,MESSAGEID:str, CHANNELID:str, ADMINMESSAGEID:str, ADMINCHANNELID:str, VOTES:dict):
    """Add a channel to the database
    
    Args:
        SERVERID (str): the discord server ID
        MESSAGEID (str): the disdcord vote controll message ID
        CHANNELID (str): the discord message channel ID (for get the message object from discord)
        ADMINMESSAGEID (str): the disdcord vote controll message ID
        ADMINCHANNELID (str): the discord message channel ID (for get the message object from discord)
        VOTES (dict): the dict who contains alls votes categories and results
    """    
    conn = __openDb(SERVERID)
    c = conn.cursor()
    try:
        data = {"a": ADMINMESSAGEID, "b": ADMINCHANNELID, "c": MESSAGEID, "d": CHANNELID}
        c.execute(f"INSERT INTO votes VALUES(:a, :b, :c, :d)", data)
    except:
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS votes(
            adminmessageid text,
            adminchannelid text,
            messageid text,
            channelid text
        )""")
        data = {"a": ADMINMESSAGEID, "b": ADMINCHANNELID, "c": MESSAGEID, "d": CHANNELID}
        c.execute(f"INSERT INTO votes VALUES(:a, :b, :c, :d)", data)

    conn.commit()
    conn.close()
    writeVotes(ADMINMESSAGEID, {})

def getVote(ADMINMESSAGEID:str):
    with open(os.path.join(".","core","data","votes_categories.json"), "r") as f:
        content = json.load(f)
    return content[ADMINMESSAGEID]

def getVotefile():
    with open(os.path.join(".","core","data","votes_categories.json"), "r") as f:
        content = json.load(f)
    return content

def removeVote(SERVERID:str, VOTEMESSAGEID:str):
    """remove a channel from the database

    Args:
        SERVERID (str): the discord server ID
        VOTEMESSAGEID (str): the discord vote controll message ID
    """    
    conn = __openDb(SERVERID)
    c = conn.cursor()
    c.execute(f"DELETE FROM votes WHERE adminmessageid= {VOTEMESSAGEID}")

    conn.commit()
    conn.close
    
    data = getVotefile()
    del data[VOTEMESSAGEID]
    writeVotes(VOTEMESSAGEID,data) 
    

def removeChannel(SERVERID:str, CHANNELID:str):
    """remove a channel from the database

    Args:
        SERVERID (str): the discord server ID
        CHANNELID (str): the discord channel ID
    """    
    conn = __openDb(SERVERID)
    c = conn.cursor()
    c.execute(f"DELETE FROM stackedchannels WHERE chanelid= {CHANNELID}")

    conn.commit()
    conn.close

def addChannel(SERVERID:str,CHANELID:str, PRIVATE:str):
    """Add a channel to the database
    
    Args:
        SERVERID (str): the discord server ID
        CHANELID (str): the disdcord voice channel ID
        PRIVATE (str): if the private argument is true or false
    """    
    conn = __openDb(SERVERID)
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

def addActivechannel(CHANNELID:str, private:str):
    """add the specified channel to the active stacked channel json file

    Args:
        CHANNELID (str): the discord channel ID
        private (str): if the channel is private or no
    """
    with open(os.path.join(".","core","data","activechannels.json"), "r") as f:
        content = json.load(f)
    content[CHANNELID] = private
    with open(os.path.join(".", "core", "data", "activechannels.json"), "w") as f:
        json.dump(content, f)

def removeActivechannel(CHANNELID:str):
    """remove the specified channel from the active stacked channel json file

    Args:
        CHANNELID (str): the discord channel ID
    """    
    with open(os.path.join(".","core","data","activechannels.json"), "r") as f:
        content = json.load(f)
    del content[CHANNELID]
    with open(os.path.join(".", "core", "data", "activechannels.json"), "w") as f:
        json.dump(content, f)

def getActiveChannels():
    """return the content of the active stacked channel json file

    Returns:
        list: the active stacked channel list
    """
    with open(os.path.join(".","core","data","activechannels.json"), "r") as f:
        content = json.load(f)
        return content

def getActiveChannelsPrivate(CHANNELID:str):
    """return if the gived discord channel is private or no

    Args:
        CHANNELID (str): the discord channel ID

    Returns:
        str: if the given channel is private or no
    """
    with open(os.path.join(".","core", "data", "activechannels.json"), "r") as f:
        content = json.load(f)
        return content[1].get(CHANNELID)


def addDelatableMessage(messageid:str, channelid:str):
    """add a message to the delatablemessages json file

    Args:
        messageid (str): the discord message id
    """
    with open(os.path.join(".","core","data","delatablemessages.json"), "r") as f:
        content = json.load(f)
    content[messageid] = channelid
    with open(os.path.join(".", "core", "data", "delatablemessages.json"), "w") as f:
        json.dump(content, f)                

def removeDelatableMessage(messageid:str):
    """remove a message from the delatablemessages json file

    Args:
        messageid (str): the discord message id
    """
    with open(os.path.join(".","core","data","delatablemessages.json"), "r") as f:
        content = json.load(f)
    del content[messageid]
    with open(os.path.join(".", "core", "data", "delatablemessages.json"), "w") as f:
        json.dump(content, f)

def getDelatableMessages():
    """return the dict of all delatable messages file

    Returns:
        dict: the dict who contain alls the delatable messages
    """
    with open(os.path.join(".", "core", "data", "delatablemessages.json"), "r") as f:
        content = json.load(f)
        return content

