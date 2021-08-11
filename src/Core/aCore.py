from src.environment.dateTime import GetDateTime

class aCore():
    def __init__(self,name,nonse,PluginsList,ScriptList):
        GetData(self,name,nonse,PluginsList,ScriptList)

    
def GetData(self,name,nonse,PluginsList,ScriptList):
        if name is None:
            self.aName=str("Gideon")
        else:
            self.aName=str(name)

        if nonse is None:
            self.aNonse="000"
        else:
            self.aNonse=nonse
        
        if PluginsList is None:
            self.aPlugins="0"
        else:
            self.aPlugins=PluginsList

        if ScriptList is None:
            self.aScriptList=[]
            
        else:
            self.aScriptList=ScriptList
        self.aDateTimeStart=GetDateTime()