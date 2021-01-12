from kitchen.ingredients.Ingredient import LemonZest
from kitchen.ingredients.Collections import ChilledCollection
from kitchen import Rosemary
from kitchen.utensils import Fridge, Bowl, Oven, PieDish, Plate
from kitchen.ingredients import Flour, Water, Salt, Butter, Apple, Lemon, Sugar, Cornstarch, Cinnamon, Egg

# Preparing the chilled dough
fridge = Fridge.use()
bowl_water = Bowl.use(name = "water")
bowl_water.add(Water.take(ml = 200))
fridge.add(bowl_water)
chilled_water = fridge.take()

bowl_dough = Bowl.use(name = "dough")
bowl_dough.add(Flour.take(grams= 300))
bowl_dough.add(Salt.take('a teaspoon'))
for i in range (25): 
    butter = Butter.take(grams = 10)
    bowl_dough.add(butter)
    bowl_dough.mix()
bowl_dough.add(chilled_water.take())

fridge.add(bowl_dough)
chilled_dough = fridge.take()

Rosemary.taste(chilled_dough)

# Preparing the filling
bowl_filling = Bowl.use(name = "filling")
for i in range(6): 
    apples = Apple.take()
    apples.peel()
    bowl_filling.add(apples)

lemon = Lemon.take(1)
lemon_zest = lemon.zest()
lemon_juice = lemon.squeeze()

bowl_filling.add(Sugar.take(grams = 150))
bowl_filling.add(Cornstarch.take("a spoonful"))
bowl_filling.add(Salt.take("a pinch"))
bowl_filling.add(Cinnamon.take("a teaspoon"))
bowl_filling.add(lemon_zest.take("1/2"))
bowl_filling.add(lemon_juice.take("1/2"))
bowl_filling.mix()

Rosemary.taste(bowl_filling)

# Preparing the spreads
bowl_layer = Bowl.use(name = "spreads")
egg = Egg.take(1)
egg.crack()
bowl_layer.add(egg)
bowl_layer.add(Sugar.take("a spoon"))
bowl_layer.add(lemon_zest.take("1/2"))
bowl_layer.add(lemon_juice.take("1/2"))
bowl_layer.mix()

Rosemary.taste(bowl_layer)

# Preparing the pie
plate = Plate.use(name = "apple pie")
preheated_oven = Oven.use(degrees= 180)

piedish = PieDish.use (name = "apple pie")
piedish.add(chilled_dough.take("3/4"))
piedish.add(bowl_filling.take())
piedish.add(chilled_dough.take("1/4"))
piedish.add(bowl_layer.take())
preheated_oven.add(piedish)
preheated_oven.bake(minutes = 60)

plate.add(piedish.take())
Rosemary.serve(plate)