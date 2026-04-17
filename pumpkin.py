from helpers import *
from planting import *


def regulate_supply():
	if num_items(Items.Carrot) < 1000:
		goto(0,0)
		navigate_farm(pcarrot, 6, 6)
  
	if num_items(Items.Wood) < 1000 or num_items(Items.Hay) < 1000:
		goto(6,0)
		navigate_farm(ptree, 6, 6)
  
	if num_items(Items.Power) < 200:
		goto(0,12)
		psunflower()

while True:
	regulate_supply()
	goto(0,6)
	ppumpkin()