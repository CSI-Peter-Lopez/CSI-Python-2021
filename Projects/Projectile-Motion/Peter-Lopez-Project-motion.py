gun = "APB"
caliber = "9x18mm Makarov"
amunicion = "9x18mm PM SP7 gzh"
velocity_ms = 420

Building = "Oriental Plaza"
BuildingHeight = 209.974

gravity_Ms = 9.81

import math

time__s = math.sqrt((2 * BuildingHeight) / gravity_Ms)

print(f"The gun selected for the experiment is {gun}. Whith the caliber {caliber}, amunicion {amunicion} with a velocity of {velocity_ms}. We will shoot from the {Building} building with a height of {BuildingHeight}.")