try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

def Procurar():
    print("Pesquisa")
    query = input("Google...")
    for j in search(query, tld="com", num=10, stop=10, pause=2):
        print(j)
