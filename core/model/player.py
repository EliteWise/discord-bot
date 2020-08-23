class Player:

    def __init__(self, uuid, name, top1, kills, deaths):
        self.uuid = uuid
        self.name = name
        self.top1 = top1
        self.kills = kills
        self.deaths = deaths

    def getUUID(self):
        return self.uuid

    def getName(self):
        return self.name

    def getTop1(self):
        return self.top1

    def getKills(self):
        return self.kills

    def getDeaths(self):
        return self.deaths

    def setUUID(self, uuid):
        self.uuid = uuid

    def setName(self, name):
        self.name = name

    def setTop1(self, top1):
        self.top1 = top1

    def setKills(self, kills):
        self.kills = kills

    def setDeaths(self, deaths):
        self.deaths = deaths
