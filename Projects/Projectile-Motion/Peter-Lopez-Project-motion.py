import math

# gun = "APB"
# caliber = "9x18mm Makarov"
# amunicion = "9x18mm PM SP7 gzh"
# velocity_ms = 420

# Building = "Oriental Plaza"
# BuildingHeight = 209.974 

# gravity_ms = 9.81


time_s = math.sqrt((2 * BuildingHeight) / gravity_Ms)

def ProjectileFuction(gun:str, caliber:str, amunicion:str, velocity_ms: int, Buildong:str, BuildingHeight: int, gravity_ms: int):
    time_s = math.sqrt((2 * BuildingHeight) / gravity_Ms)
    ditance_m = (velocity_ms * time_s)
    
    print(f"The gun selected for the experiment is {gun}. Whith the caliber {caliber}, amunicion {amunicion} with a velocity of {velocity_ms}. We will shoot from the {Building} building with a height of {BuildingHeight}.")


ProjecttileFunction("APB", "9x18mm Makarov", "9x18mm PM SP7 gzh", 420, "Oriental Plaza", 209.974, 9.81)