from src.Core.aCore import aCore
from src.plugins.customs.scripts.GSearch.search import Procurar
from src.plugins.customs.CoinMarketCap.CMC_API import getAll

def __main__():
    getAll()



def UsoScript():
    esc=input("Escolha. 1- Procurar/ 2-sdads")
    if esc ==1:
        Procurar()
    else:
        return
    return


__main__()


