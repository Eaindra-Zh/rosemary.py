from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Milk, Egg, Flour, Salt, Butter 
from random import randint

bowl = Bowl.use(name = "batter")
n = randint (1,5)

# Whisking the 2 eggs.
for eggs in Egg.take(2*n):
    eggs.crack()
    bowl.add(eggs)
bowl.mix()

# Adding salt and mixing flour in batches of 50 grams 5 times. 
bowl.add(Salt.take("dash"))
for i in range(5*n):
    flour = Flour.take(grams = 50)
    bowl.add(flour)
    bowl.mix()

# Adding half of the milk, mix and then adding another half. 
for i in range (2*n): 
    milk = Milk.take(ml = 250)
    bowl.add(milk)
    bowl.mix()

Rosemary.taste(bowl)  

plate = Plate.use(name = "pancakes")

# Cooking 4 pancakes for 1 minutes to each side. 
for i in range (8*n):
    greased_pan = Pan.use(name = "pancakes")
    greased_pan.add(Butter.take("slice"))
    greased_pan.add(bowl.take(f'1/{8*n}'))
    greased_pan.cook(minutes = 1)
    greased_pan.flip()
    greased_pan.cook(minutes = 1)
    plate.add(greased_pan.take())

Rosemary.serve(plate)


