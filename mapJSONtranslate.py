import json

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
for tile in mapJSON["tiles"]:
    tileId = tile["tileId"]
    if (tileId != "Hills" and tileId != "Forest" and tileId != "Grasslands" and tileId != "Ocean" and tileId != "Coast"):
        centerX = tile["pos"]["x"]
        centerY = tile["pos"]["y"]
        biomeCount = [[0, 0, "Grasslands"], [0, 1, "Hills"], [0, 2, "Forest"]]
        for searchTile in mapJSON["tiles"]:
            searchX = searchTile["pos"]["x"]
            searchY = searchTile["pos"]["y"]
            if((centerY == searchY or centerY-1 == searchY) and (centerX == searchX or centerX-1 == searchX or centerX+1 == searchX)):
                if searchTile["tileId"] == "Grasslands":
                    biomeCount[0][0] += 1
                elif searchTile["tileId"] == "Hills":
                    biomeCount[1][0] += 1
                elif searchTile["tileId"] == "Forest":
                    biomeCount[2][0] += 1
        tile["tileId"] = max(biomeCount)[2]

width = mapJSON["bounds"]["max"]["x"] + 1
height = mapJSON["bounds"]["max"]["y"] + 1
mapJSONtranslated = {
    "cells": [[None for x in range(height)] for y in range(width)],
    "width": width,
    "height": height
}
for tile in mapJSON["tiles"]:
    tileX = tile["pos"]["x"]
    tileY = tile["pos"]["y"]
    mapJSONtranslated["cells"][tileX][tileY] = {
        "biome": tile["tileId"]
    }
    if "city" in tile: mapJSONtranslated["cells"][tileX][tileY]["city"] = True
    if "river" in tile: mapJSONtranslated["cells"][tileX][tileY]["river"] = True
    if "road" in tile: mapJSONtranslated["cells"][tileX][tileY]["road"] = True
file = open(r"assets\maps\overworld11.json", "w")
json.dump(mapJSONtranslated, file)
file.close()

# (0,+1) (0,-1) (-1,-1) (-1, 0) (+1,-1) (+1,0)