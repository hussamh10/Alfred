from modules.games import Games

def parse(query):
    obj = None
    q = None

    if "toss" in query:
        obj = Games()
        q = "toss"

    if "RPS" in query:
        obj = Games()
        q = "rps"


    return obj, q
