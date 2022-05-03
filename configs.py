import ast

def getConfig(name):
    file = open(name, "r")
    text = file.read()
    return ast.literal_eval(text)

class config:
    main = getConfig("config.json")
    display = main["display"]
    fps = main["fps"]
