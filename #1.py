#Extra Measures
areaPaint = float(input("How much area does your litre of paint cover?: "))
areaRoll = float(input("How much area does your roll of wallpaper cover?: "))
areaTile = float(input("How much area does 1 of your tiles cover?: "))
#1
l = float(input("Enter length of room: "))
b = float(input("Enter breadth of room: "))
h = float(input("Enter Height of room: "))
#2
areaFloor = l * b
areaWall = l * h * 4
#3
numTiles = areaFloor / areaTile
numRolls = areaWall / areaRoll
litresPaint = areaFloor / areaPaint
#4
print("You'll need:",numTiles,"tiles,",numRolls,"rolls of wallpaper, and",litresPaint,"litres of paint.")