from helpers import *
from planting import *


def regulate_supply():
	
	target_supply = 10000
	if num_items(Items.Carrot) < target_supply:
		goto(0,0)
		navigate_farm(pcarrot, 6, 6)
		return True

	if num_items(Items.Wood) < target_supply or num_items(Items.Hay) < target_supply:
		goto(6,0)
		navigate_farm(ptree, 6, 6)
		return True

	if num_items(Items.Power) < 300:
		goto(0,12)
		psunflower(6,4)
		return True

	if num_items(Items.Weird_Substance) < target_supply:
		goto(3,14)
		pweird()
		return True

	if num_items(Items.Pumpkin) < target_supply:
		goto(0,6)
		ppumpkin(6)
		return True

	if num_items(Items.Cactus) < target_supply:
		goto(6,6)
		pcactus(6,6)
		return True

clear()
while True:
	while regulate_supply():
		continue
	goto(3,3)
	pweird()