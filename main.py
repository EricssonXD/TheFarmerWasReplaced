from helpers import *
from planting import *


def regulate_supply():
	if num_items(Items.Carrot) < 1000:
		goto(0,0)
		navigate_farm(pcarrot, 6, 6)
  
	if num_items(Items.Wood) < 1000 or num_items(Items.Hay) < 1000:
		goto(6,0)
		navigate_farm(ptree, 6, 6)
  
	if num_items(Items.Power) < 300:
		goto(0,12)
		psunflower()

	if num_items(Items.Weird_Substance) < 1000:
		goto(3,14)
		pweird()

	if num_items(Items.Pumpkin) < 1000:
		goto(0,6)
		pcactus(6,6)

	if num_items(Items.Cactus) < 1000:
		goto(6,6)
		pcactus(6,6)


while True:
	regulate_supply()
	goto(10,1)
	pweird()
