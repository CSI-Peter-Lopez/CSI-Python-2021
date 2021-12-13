import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json


# gun = "APB"
# caliber = "9x18mm Makarov"
# amunicion = "9x18mm PM SP7 gzh"
# velocity_ms = 420

# Building = "Oriental Plaza"
# BuildingHeight = 209.974

# gravity_ms = 9.81

# Convert your variables into parameters

def ProjectileFunction(experimentalData: ExperimentalData):

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet = planets.index(experimentalData.planet)
    time_s = math.sqrt((2 * experimentalData.BuildingHeight) / g_ms2[planet])

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)
    
    print(f"The gun selected for the experiment is {experimentalData.gun}. Whith the caliber {experimentalData.caliber}, amunicion {experimentalData.ammunition} with a velocity of {experimentalData.velocity_ms}. We will shoot from the {experimentalData.Building} building with a height of {experimentalData.BuildingHeight}.")
    print(f"The experiment is carried out in {experimentalData.planet} with a gravity of {g_ms2[planet]}")


# Convert your script parameters into a single JSON object
# experimentalData = {

# "gun": "APB",
# "caliber":  "9x18mm Makarov",
# "amunicion": "9x18mm PM SP7 gzh",
# "velocity_ms": 420,
# "Building":  "Oriental Plaza",
# "BuildingHeight": 209.974,
# "gravity_ms": 9.81,

# }

# experimentalData = ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM SP7 gzh", 420, "Oriental Plaza", 209.974, 9.81)


myDataSet = [
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM SP7 gzh", 420, "Oriental Plaza", 209.974, "Earth"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM BZhT gzh", 325, "Oriental Plaza", 209.974, "Mars"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM P gzh", 302, "Oriental Plaza", 209.974, "Venus"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM PBM gzh", 519, "Oriental Plaza", 209.974, "Saturn"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM SP8 gzh", 250, "Oriental Plaza", 209.974, "Mercury"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM RG028 gzh", 330, "Oriental Plaza", 209.974, "Jupiter"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM PSV", 280, "Oriental Plaza", 209.974, "Neptune"),
ExperimentalData("APB", "9x18mm Makarov", "9x18mm PM Pst gzh", 298, "Oriental Plaza", 209.974, "Uranus")

]

for data in myDataSet:
    print("\n--------------------------------------\n")
    ProjectileFunction(data)

# Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

print(myOutputFilePath)

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

# Deserialization
deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n--------------------------------------\n")
    ProjectileFunction(ExperimentalData(**e))

# ProjectileFuction(experimentalData)