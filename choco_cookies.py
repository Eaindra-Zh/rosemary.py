from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, BakingTray, Plate
from kitchen.ingredients import Butter, Egg, Salt, Sugar, Flour, ChocolateChips, BakingPowder

bowl = Bowl.use(name = "batter")

# Adding sugar to the butter in bits
bowl.add(Butter.take('1/2'))
for i in range(10):
    sugar = Sugar.take(grams=20)
    bowl.add(sugar)
    bowl.mix()

# Adding 2 eggs and some salt into the mixture
for eggs in Egg.take(2):
    eggs.crack()
    bowl.add(eggs)
bowl.add(Salt.take("a pinch"))
bowl.mix()

# Adding flour and chocolate chips
bowl.add(Flour.take(grams= 300))
bowl.add(ChocolateChips.take(grams= 200))
bowl.add(BakingPowder.take("a packet"))
bowl.mix()

Rosemary.taste(bowl)

plate = Plate.use(name = "chocolate chip cookies")

# Preheating the oven

preheated_oven = Oven.use(degrees= 175)
bakingtray = BakingTray.use (name = "chocolate chip cookie")

# Baking the 16 cookies
for cookies in range(16):
    bakingtray.add(bowl.take("1/16"))
    
preheated_oven.add(bakingtray)
preheated_oven.bake (minutes=10)
plate.add(bakingtray.take())

Rosemary.serve(plate)


