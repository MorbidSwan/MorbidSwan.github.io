import json
import math

file = open(r"assets\maps\hexton-hills - Nala_ overworld (11).json", "r")
mapJSON = json.load(file)
file.close()
for tile in mapJSON["tiles"]:
    tileIdType = tile["tileId"][0:2]
    if tileIdType == "AH":
        tile["tileId"] = "Hills"
    elif tileIdType == "AW":
        tile["tileId"] = "Forest"
    elif tileIdType == "AP":
        tile["tileId"] = "Grasslands"
    elif tileIdType == "AO":
        tile["tileId"] = "Ocean"
    elif tileIdType == "AC":
        tile["tileId"] = "Coast"
    elif tileIdType == "AF":
        tile["city"] = True
    elif tileIdType == "AV":
        tile["river"] = True
    elif tileIdType == "AR":
        tile["road"] = True
    elif tileIdType == "AB":
        tile["road"] = True
        tile["river"] = True

width = math.ceil((mapJSON["bounds"]["max"]["x"] + 1)/2) + 2
height = mapJSON["bounds"]["max"]["y"] + 3
mapJSONtranslated = {
    "cells": [[[None for x in range(height)] for y in range(width)], [[None for a in range(height)] for b in range(width)]],
    "width": width,
    "height": height
}
for tile in mapJSON["tiles"]:
    tileX = math.floor((tile["pos"]["x"])/2) + 1
    tileY = height-tile["pos"]["y"]-2
    tileA = (tile["pos"]["x"])%2
    print("X: "+str(tileX))
    print("Y: "+str(tileY))
    print("A: "+str(tileA))
    mapJSONtranslated["cells"][tileA][tileX][tileY] = {
        "biome": tile["tileId"]
    }
    if "city" in tile: mapJSONtranslated["cells"][tileA][tileX][tileY]["city"] = True
    if "river" in tile: mapJSONtranslated["cells"][tileA][tileX][tileY]["river"] = True
    if "road" in tile: mapJSONtranslated["cells"][tileA][tileX][tileY]["road"] = True

for idxA, array in enumerate(mapJSONtranslated["cells"]):
    for idxX, x in enumerate(array):
        for idxY, tile in enumerate(x):
            if tile != None:
                tileBiome = tile["biome"]
                if (tileBiome != "Hills" and tileBiome != "Forest" and tileBiome != "Grasslands" and tileBiome != "Ocean" and tileBiome != "Coast"):
                    biomeCount = [[0, 0, "Grasslands"], [0, 1, "Hills"], [0, 2, "Forest"], [0, 3, "Ocean"]]
                    for searchTile in [mapJSONtranslated["cells"][idxA][idxX][idxY-1], mapJSONtranslated["cells"][idxA][idxX][idxY+1], mapJSONtranslated["cells"][1-idxA][idxX-1+idxA][idxY-1+idxA], mapJSONtranslated["cells"][1-idxA][idxX-1+idxA][idxY+idxA], mapJSONtranslated["cells"][1-idxA][idxX+idxA][idxY-1+idxA], mapJSONtranslated["cells"][1-idxA][idxX+idxA][idxY+idxA]]:
                        if searchTile != None:
                            if searchTile["biome"] == "Grasslands":
                                biomeCount[0][0] += 1
                            elif searchTile["biome"] == "Hills":
                                biomeCount[1][0] += 1
                            elif searchTile["biome"] == "Forest":
                                biomeCount[2][0] += 1
                            elif searchTile["biome"] == "Ocean":
                                biomeCount[3][0] += 1
                    tile["biome"] = max(biomeCount)[2]


file = open(r"assets\maps\overworld11.json", "w")
json.dump(mapJSONtranslated, file)
file.close()
