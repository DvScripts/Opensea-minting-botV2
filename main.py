import os
import json
import opensea

def getConfig():
        configFile = open("config.json", 'r')
        return list(json.load(configFile).values())

config = getConfig()

isWindows = True if os.name == 'nt' else False

if "opensea.io" in config[0]:
    print("Found opensea.io link")
    opensea.mint(config, isWindows)

else:
    print("Could not recognize link")

