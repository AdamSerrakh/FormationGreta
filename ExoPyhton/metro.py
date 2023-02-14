import requests
import json

def affichage(liste):

    monresultat =''
    for undict in liste:
        if undict["name"][0] == 'L':
            monresultat += f'\t\t{undict["name"]} \t{undict["route_name"]}\n'
    return monresultat

def recherche(marecherche):
    global monjson
    if marecherche == "help":
        return """
                Pour voir la direction d'une ligne, ex : Ligne 1
                Pour voir toutes les directions disponible : tous
                Pour quitter, utilisez CTRL+C
               """
    elif marecherche == "tous":
        return affichage(monjson)
    else :
        for undict in monjson:
            if undict["name"] == marecherche:
                return f'\t\t{undict["route_name"]}\n'
        return f'\t\tPas de résultat pour {marecherche}\n'
        
"""
with open('metros.json') as file:
    data = file.read()
    #print(data)
    monjson = json.loads(data)
    #print(type(monjson))
    #print(monjson.keys())
    #print(monjson['result'].keys())
    #print(monjson['result']['metros'])
    #print(affichage(monjson['result']['metros']))
"""
data=requests.get('https://api-ratp.pierre-grimaud.fr/v4/lines').text
data=requests.get('https://gist.githubusercontent.com/aliou/065689914b6677cfb06c/raw/a0d973e81c3ff4fbea706950ccdb01c555f66600/metro-lines.json').text

monjson = json.loads(data)
#print(monjson)

try :
    while True:
        print(recherche(input("Quelle direction de ligne souhaitez vous consulter (help)? ")))
except KeyboardInterrupt:
    print("Au revoir et à bientôt")
