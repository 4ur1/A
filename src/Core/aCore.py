from src.environment.dateTime import GetDateTime
 
class aCore():
    def __init__(self, *data):
        GetData(self, data)

def GetData(self, data):
    self.aDateTimeStart = GetDateTime()
    if data is None:
        self.aName = str("Gideon")
        self.aNonse = "000"
        self.aPlugins = "0"
        self.aScriptList = "DEFAULT SCRIPTS"
    else:
        self.aName = str(data[0])
        self.aNonse = data[1]
        self.aPlugins = data[2]
        self.aScriptList = data[3]
    